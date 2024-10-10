from secrets import token_hex
import time
from common.constants import script_dir
from pysqlcipher3 import dbapi2 as securesql

print(script_dir)
# todo: add delete user, modify user info

class secureSql:

    def __init__(self):
        db_folder = "data"
        utilities_dir = "common"
        key_db_name = "keys"
        user_db_name = "private"
        self.key_db_path = f"{script_dir}/{utilities_dir}/{db_folder}/{key_db_name}.db"
        self.user_db_path = f"{script_dir}/{utilities_dir}/{db_folder}/{user_db_name}.db"

    
    def authenticate(
            self,
            id: str,
            passwd: str,
            key_db_pass: str,
            access_db: bool = False
    ):
            # connect to key db
            key_db = securesql.connect(self.key_db_path)
            key_db_cursor = key_db.cursor()
            # try statement to catch error in authentication
            try:
                # connect to key db, fetch user db key
                key_db_cursor.executescript(
                    f"""
                    PRAGMA key = '{key_db_pass}';

                    PRAGMA cipher_compatibility = 3;
                    
                    """
                )

                key_db_cursor.execute("""select user_db_key from keys""")
            
                #parse out user db key
                data = key_db_cursor.fetchall()
                user_db_key = data[0][0]
                #close key db
                key_db.close()

                user_db = securesql.connect(self.user_db_path)
                user_db_cursor = user_db.cursor()
            
                user_db_cursor.executescript(
                    f"""
                    PRAGMA key = '{user_db_key}';

                    PRAGMA cipher_compatibility = 3;
                    """
                ) #fix select statement
                user_db_cursor.execute(f"""select passwd_hash, is_admin from users where user_id=? and passwd_hash=?""", (id, passwd))
                data = user_db_cursor.fetchall()
                user_error = False
                if data[0][0] == passwd:
                    pass
                else:
                    user_error = True
                if data[0][1] == 1:
                    is_admin = True
                else:
                    is_admin = False
                user_db.close()
                if user_error:
                    print("The username or password was incorrect")
                    return user_error # migrate over to flask
                #different output depending on usage
                if not user_error:
                    if access_db:
                        return user_db_key , is_admin
                    if not access_db:
                        #added for readability
                        key_error = False
                        return key_error

            except:
                key_db.close()
                #added for readability
                key_error = True
                return key_error # migrate over to flask
        
    def getUserInfo(
        self,
        key_db_token: str,
        user_id: str,
        passwd_hash: str,
        email_login: bool = False,
        is_admin: bool = False,
        callsign: bool = False,
        key_id: bool = False
    ):
        
        # try:
        error = False
        if key_db_token == None:
            print("Database encryption key was not passed.")
            error = True
        # try:
        print("db path: ", self.user_db_path)
        user_db_key, is_admin = self.authenticate(id=user_id, passwd=passwd_hash, key_db_pass=key_db_token)
        user_db = securesql.connect(self.user_db_path)
        user_db_cursor = user_db.cursor()
        user_db_cursor.executescript(
            f"""PRAGMA key='{user_db_key}';

                PRAGMA cipher_compatibility = 3
            """
            )
        # except:
            # print("Database key is incorrect.")
            # error = True
        if user_id == None or passwd_hash == None:
            print("Either the user_id or password hash was not passed.")
            error = True
        if error:
            return error, ''
        if email_login or is_admin or key_id or callsign:
            user_db_cursor.execute(f"""select config_id from users where user_id={user_id} and passwd_hash={passwd_hash}""")
            config_id = user_db_cursor.fetchall()
            if email_login  and not is_admin and not key_id and not callsign:
                user_db_cursor.execute(f"""select email, email_passwd from vars where config_id={config_id}""")
                data = user_db_cursor.fetchall()
                info = {'email': data[0][0], 'email_passwd': data[0][1]}
            if not email_login and not is_admin and key_id and not callsign:
                info = {"key_id": config_id}
        if not email_login  and is_admin and not key_id and not callsign:
            info = {"is_admin": is_admin}
        if not email_login and is_admin and not key_id and callsign:
            if is_admin:
                user_db_cursor.execute(f"""select callsign from users where user_id={user_id} and passwd_hash={passwd_hash}""")
                data = user_db_cursor.fetchall()
                info = {"callsign": data[0][0]}

        # except:
            # error = True
            # print("An unknown error occured.")
            # return error, {}

        # error = False
        # return error, info


        
    def buildUserInfo(
        self,
        auth_user_id: str,
        auth_user_passwd: str,
        key_db_token: str,
        email: str,
        email_passwd: str,
        key_id: str,
        satnogs_cookie, # this will be a file in the form of hex or binary
        n2yo_key: str,
        callsign: str = None,
        create_admin: bool = False
    ):


        try:
            #authenticate
            user_db_key, admin_user = self.authenticate(id=auth_user_id, passwd=auth_user_passwd, key_db_token=key_db_token)
            if not admin_user:
                error = True
                return  error # migrate to flask
            else:
                user_db = securesql.connect(secureSql.user_db_path)
                user_db_cursor = user_db.cursor()
                
                #create admin variable
                if create_admin:
                    is_admin = 1
                else: 
                    is_admin = 0

                # create ids
                user_id = token_hex(16)
                config_id = token_hex(16)
                passwd_hash = token_hex(1024)

                #create user
                user_db_cursor.executescript(
                    f"""
                    PRAGMA key = '{user_db_key}';

                    PRAGMA cipher_compatibility = 3;
                    
                    insert into users (user_id, passwd_hash, is_admin, callsign, creation_time, config_id) values ({user_id}, {passwd_hash}, {is_admin}, {callsign}, {time.time()}, {config_id})

                    insert into vars (config_id, email, email_passwd, key_id, n2yo_key) values ({config_id}, {email}, {email_passwd}, {key_id}, {satnogs_cookie} {n2yo_key})
                    """
                    )
                user_db.commit()
                user_db.close()
            
                error = False
                return error, {'user_id': user_id, 'passwd': passwd_hash}
        except:
            print("An error occured during authetication.")
            error = True
            return error # migrate over to flask
        
        
    def deleteUser(
        self,
        auth_user_id: str,
        auth_user_passwd: str,
        key_db_token: str,
        user_id: str # id of user you want to delete
        
    ):


        try:
            #authenticate
            user_db_key, admin_user = self.authenticate(id=auth_user_id, passwd=auth_user_passwd, key_db_token=key_db_token)
            if not admin_user:
                error = True
                return error # migrate to flask
            else:
                user_db = securesql.connect(secureSql.user_db_path)
                user_db_cursor = user_db.cursor()
            

                #create user
                user_db_cursor.executescript(
                    f"""
                    PRAGMA key = '{user_db_key}';

                    PRAGMA cipher_compatibility = 3;

                    select config_id from users where user_id={user_id}"""
                )
                config_id = user_db_cursor.fetchall()[0][0]
                user_db_cursor.executescript(
                    f"""
                    delete from users where user_id={user_id};

                    delete from vars where config_id={config_id}
                    """
                    )
                user_db.commit()
                user_db.close()
            
                error = False
                return error #migrate over to flask
        except:
            print("An error occured during authetication.") #migrate over to flask
            error = True
            return error
        