from secrets import token_hex
import time
from common.constants import script_dir
from pysqlcipher3 import dbapi2 as securesql

print(script_dir)
# todo: add delete user, modify user info
# if error=False, then no error, vice versa

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
                #connect to key db, fetch user db key
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
            
    # note: using this function with the admin user created with the database
    # (that does not have data for all fields) may bring up unknown errors,
    # and this use case should be avoided.
    def getUserInfo(
        self,
        key_db_token: str,
        user_id: str,
        passwd_hash: str,
        email_login: bool = False,
        is_admin: bool = False,
        callsign: bool = False,
        key_id: bool = False,
        creation_time: bool = False
    ):
        final_json = {}
        error_message = ""
        try:
            error = False
            try:
                print("db path: ", self.user_db_path)
                # gets user_db key, and confirms admin status
                user_db_key, admin_check = self.authenticate(id=user_id, passwd=passwd_hash, key_db_pass=key_db_token, access_db=True)
                print("passed auth")
                user_db = securesql.connect(self.user_db_path)
                user_db_cursor = user_db.cursor()
                user_db_cursor.executescript(
                    f"""PRAGMA key='{user_db_key}';

                        PRAGMA cipher_compatibility = 3
                    """
                    )
            except:
                error_message = "Credentials are incorrect."
                error = True
            if error:
                return error, error_message, {}
            if email_login or key_id or callsign and not is_admin and not creation_time:
                print(f"""select config_id from users where user_id=? and passwd_hash=?""", (user_id, passwd_hash))
                user_db_cursor.execute(f"""select config_id from users where user_id=? and passwd_hash=?""", (user_id, passwd_hash))
                config_id = user_db_cursor.fetchall()
                if email_login and not key_id and not callsign:
                    user_db_cursor.execute(f"""select email, email_passwd from logins where config_id=?""", (config_id,))
                    data = user_db_cursor.fetchall()
                    print(data)
                    info = {'email': data[0][0], 'email_passwd': data[0][1]}
                if not email_login and key_id and not callsign:
                    info = {"key_id": config_id}
            if not email_login  and is_admin and not key_id and not callsign and not creation_time:
                if admin_check:
                    info = {"is_admin": True}
                else:
                    info = {"is_admin": False}
            if not email_login and not is_admin and not key_id and callsign and not creation_time:
                if admin_check:
                    user_db_cursor.execute(f"""select callsign from users where user_id=? and passwd_hash=?""", (user_id, passwd_hash))
                    data = user_db_cursor.fetchall()
                    info = {"callsign": data[0][0]}
            if not email_login and not is_admin and not key_id and notcallsign:
    
        except:
            error = True
            info = {}
            error_message = "An unknown error occured."
            
            # return error
            return error, error_message, {}
        
        error = False
        print("got info:"+f"{info}")
        return error, error_message, info



        
    def buildUserInfo(
        self,
        satnogs_cookies, # this will be a file in the form of hex or binary
        auth_user_id: str,
        auth_user_passwd: str,
        key_db_token: str,
        email: str,
        email_passwd: str,
        callsign: str = None,
        create_admin: bool = False
    ):

        error_message = ""
        try:
            #authenticate
            user_db_key, admin_user = self.authenticate(id=auth_user_id, passwd=auth_user_passwd, key_db_pass=key_db_token, access_db=True)
            print("passed auth"+"\n\n\n\n\n"+user_db_key+"\n\n\n\n\n"+str(admin_user))
            if not admin_user:
                error = True
                error_message = "Authentication failed. Must be an administrator to create a new user."
                return  error, error_message, {} 
            else:
                user_db = securesql.connect(self.user_db_path)
                user_db_cursor = user_db.cursor()
                
                #create admin variable
                if create_admin:
                    is_admin = 1
                else: 
                    is_admin = 0

                # create ids
                user_id = token_hex(16)
                key_id = token_hex(16) # the key_id value is an identifier used throughout the database APIs to identify user logins and keys
                passwd_hash = token_hex(1024)

                #create user
                user_db_cursor.executescript(
                    f"""
                    PRAGMA key='{user_db_key}';

                    PRAGMA cipher_compatibility = 3
                    """)
            
                user_db_cursor.execute(
                    """
                    insert into users (user_id, passwd_hash, is_admin, callsign, creation_time, key_id)
                    values (?, ?, ?, ?, ?, ?)
                    """,
                    (user_id, passwd_hash, is_admin, callsign, time.time(), key_id)
                    )

                user_db_cursor.execute(
                    """
                    insert into logins (key_id, email, email_passwd, satnogs_cookies)
                    values (?, ?, ?, ?)
                    """,
                    (key_id, email, email_passwd, satnogs_cookies)
                    )
                user_db.commit()
                user_db.close()
            
                error = False
                # once your account is created by an admin, your data
                # will be sent over to the webserver, which will cache 
                # your key_id in the general db via its API

                # you will then get an automated email containing your user ID
                # and password from the webserver, which you can use to login via
                # an app
                return error, error_message, {'user_id': user_id, 'passwd': passwd_hash, "key_id": key_id}
        except:
            error_message = "An error occurred during user creation. Please try again."
            error = True
            return error, error_message, {} 
        
        
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

                    select config_id from users where user_id='{user_id}'"""
                )
                config_id = user_db_cursor.fetchall()[0][0]
                user_db_cursor.execute(
                    """delete from users where user_id = ?""", (user_id,)
                )

                user_db_cursor.execute(
                    """delete from logins where config_id = ?""", (config_id,)
                    )
                user_db.commit()
                user_db.close()
            
                error = False
                return error #migrate over to flask
        except:
            print("An error occured during authetication.") #migrate over to flask
            error = True
            return error
        