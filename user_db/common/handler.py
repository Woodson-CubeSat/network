from secrets import token_hex
import time
from common.constants import script_dir
from pysqlcipher3 import dbapi2 as securesql
import base64
import bcrypt
from bcrypt import hashpw, gensalt
from sqlite3 import Binary
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

    
    def authenticate(self, id: str, passwd: str, key_db_pass: str, access_db: bool = False):
        # Connect to key database
        key_db = securesql.connect(self.key_db_path)
        key_db_cursor = key_db.cursor()
        print(self.key_db_path)

        try:
            # Authenticate against the key database
            key_db_cursor.executescript(
                f"""
                PRAGMA key = '{key_db_pass}';

                PRAGMA cipher_compatibility = 3;
                """
            )
            print("passed checkpoint")
            try:
                # Fetch user database key
                key_db_cursor.execute("""select user_db_key from keys""")
            except:
                return True, "Database key is incorrect"
            data = key_db_cursor.fetchall()
            if not data:
                print("Key database is empty or corrupted.")
                return True, "Key database is empty or corrupted."
            user_db_key = data[0][0]
            key_db.close()

            # Authenticate against the user database
            user_db = securesql.connect(self.user_db_path)
            user_db_cursor = user_db.cursor()
            user_db_cursor.executescript(
                f"""
                PRAGMA key = '{user_db_key}';
                PRAGMA cipher_compatibility = 3
                """
            )

            user_db_cursor.execute(
                "SELECT passwd_hash, is_admin FROM users WHERE user_id = ?",
                (id,)
            )
            user_data = user_db_cursor.fetchone()

            if not user_data:
                print("Invalid username.")
                return True, "Invalid username."

            stored_hash, is_admin = user_data

            # Use bcrypt to verify the password
            if not bcrypt.checkpw(passwd.encode(), stored_hash.encode()):
                print("Invalid password.")
                return True, "Invalid password." 

            # If successful, return based on access_db flag
            if access_db:
                return user_db_key, bool(is_admin)
            else:
                return False, ""  # Indicating no errors

        except Exception as e:
            key_db.close()
            return True, f"Authentication error: {e}" 
   
            
    def getUserInfo(
        self,
        key_db_token: str,
        user_id: str,
        passwd: str,
        email_login: bool = False,
        is_admin: bool = False,
        callsign: bool = False,
        key_id: bool = False,
        satnogs_cookies: bool = False,
        creation_time: bool = False
    ):
        error_message = ""
        info = {
            'key_id': None,
            'is_admin': None,
            'callsign': None,
            'creation_time': None,
            'satnogs_cookies': None,
            'email_login': {
                'email': None,
                'email_passwd': None
                }
            }
        try:
            user_db_key, admin_check = self.authenticate(
                id=user_id, passwd=passwd, key_db_pass=key_db_token, access_db=True
            )
            # In this case, user_db_key is used as an error code
            if user_db_key == True:
                # In this case, admin check is the error message
                return True, admin_check, {}
            print(user_db_key)

            user_db = securesql.connect(self.user_db_path)
            user_db_cursor = user_db.cursor()

            # sqlite3 is weird so executescript must be used
            user_db_cursor.executescript(
                f"""
                PRAGMA key = '{user_db_key}';
                PRAGMA cipher_compatibility = 3;
                """
            )

            if email_login or key_id or satnogs_cookies:
                user_db_cursor.execute(
                    "SELECT key_id FROM users WHERE user_id=?", (user_id,)
                )
                data = user_db_cursor.fetchall()
                if data:
                    # same thing as key_id, just a different name
                    # this variable holds the key_id for method usage
                    config_id = data[0][0]
                if key_id:
                    info["key_id"] = config_id
                else:
                    return True, "No matching user found.", info

                if email_login:
                    user_db_cursor.execute("SELECT email, email_passwd FROM logins WHERE key_id=?", (config_id,))
                    data = user_db_cursor.fetchall()
                    if data:
                        info["email_login"]["email"] = data[0][0]
                        info["email_login"]["email_passwd"] = data[0][1]

                if satnogs_cookies:
                    user_db_cursor.execute("SELECT satnogs_cookies FROM logins WHERE key_id=?", (config_id,))
                    data = user_db_cursor.fetchall()
                    if data:
                        print(data[0][0])
                        info["satnogs_cookies"] = data[0][0] # must be decoded back into binary (base64 str -> base64 bytestring -> binary)

            if is_admin:
                info["is_admin"] = admin_check

            if callsign:
                user_db_cursor.execute(
                    "SELECT callsign FROM users WHERE user_id=?", (user_id,)
                )
                data = user_db_cursor.fetchall()
                if data:
                    info["callsign"] = data[0][0]

            if creation_time:
                user_db_cursor.execute(
                    "SELECT creation_time FROM users WHERE user_id=?", (user_id,)
                )
                data = user_db_cursor.fetchall()
                if data:
                    info["creation_time"] = data[0][0]

        except Exception as e:
            error_message = f"An error occurred: {e}"
            return True, error_message, info

        finally:
            if 'user_db' in locals():
                user_db.close()

        return False, error_message, info


    def buildUserInfo(
        self,
        satnogs_cookies,  # File in binary or hex
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
            # Authenticate the user
        
            # if authentication fails, auth function will return True and an error message
            user_db_key, admin_user = self.authenticate(
                id=auth_user_id, passwd=auth_user_passwd, key_db_pass=key_db_token, access_db=True
            )
        
            # In this case, user_db_key is used as an error code
            if user_db_key == True:
                # In this case, admin user is the error message
                return True, admin_user, {}
            print(admin_user)

            if not admin_user:
                error_message = "Authentication failed. Must be an administrator to create a new user."
                return True, error_message, {}

            # Connect to the database
            with securesql.connect(self.user_db_path) as user_db:
                user_db_cursor = user_db.cursor()
            
                # sqlite3 is weird so executescript must be used
                user_db_cursor.executescript(
                    f"""
                    PRAGMA key = '{user_db_key}';
                    PRAGMA cipher_compatibility = 3;
                    """
                )
                # Generate IDs and hash
                print(satnogs_cookies)
                user_id = token_hex(16)
                key_id = token_hex(16)
                raw_password = token_hex(256)  # Initial password
                passwd_hash = bcrypt.hashpw(raw_password.encode(), bcrypt.gensalt()).decode()  # Hash the password
                # Insert user data
                user_db_cursor.execute(
                    """
                    INSERT INTO users (user_id, passwd_hash, is_admin, callsign, creation_time, key_id)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (user_id, passwd_hash, int(create_admin), callsign, time.time(), key_id)
                )

                # Insert login data
                user_db_cursor.execute(
                    """
                    INSERT INTO logins (key_id, email, email_passwd, satnogs_cookies)
                    VALUES (?, ?, ?, ?)
                    """,
                    (key_id, email, email_passwd, satnogs_cookies)
                )
                user_db.commit()

            error = False
            return error, error_message, {'UserID': user_id, 'Password': raw_password, 'key_id': key_id}
        except Exception as e:
             error_message = f"An error occurred: {e}"
             return True, error_message, {'user_id': None, 'passwd': None, 'key_id': None} 
        finally:
            if 'user_db' in locals():
                user_db.close()
        
    def deleteUser(
        self,
        auth_user_id: str,
        auth_user_passwd: str,
        key_db_token: str,
        user_id: str # id of user you want to delete
        
    ):


        try:
            #authenticate
            
            print("got here")
            # if authentication fails, auth function will return True and an error message
            user_db_key, admin_user = self.authenticate(
                id=auth_user_id, passwd=auth_user_passwd, key_db_pass=key_db_token, access_db=True
            )
            # In this case, user_db_key is used as an error code
            if user_db_key == True:
                # In this case, admin user is the error message
                return True, admin_user
            print(user_db_key)
            
            if not admin_user:
                error = True
                return error, "" 
            else:
                with securesql.connect(self.user_db_path) as user_db:
                    user_db_cursor = user_db.cursor()
            
                    # sqlite3 is weird so executescript must be used
                    user_db_cursor.executescript(
                        f"""
                        PRAGMA key = '{user_db_key}';
                        PRAGMA cipher_compatibility = 3;
                        """
                    )
                    #create user
                    user_db_cursor.execute(
                        "select key_id from users where user_id=?",
                        (user_id,)
                    )
                try:
                    key_id = user_db_cursor.fetchall()[0][0]
                except:
                    return True, "The user you want to delete does not exist."
                user_db_cursor.execute(
                    """delete from users where user_id = ?""", (user_id,)
                )

                user_db_cursor.execute(
                    """delete from logins where key_id = ?""", (key_id,)
                    )
                user_db.commit()
                user_db.close()
            
                error = False
                print(error)
                return error, "" #migrate over to flask
                
        except Exception as e:
            print(e)
            error_message = f"An error occured: {e}" #migrate over to flask
            error = True
            return error, error_message
        finally:
            if 'user_db' in locals():
                user_db.close()

    def updateUserInfo(
        self,
        key_db_token: str,
        satnogs_cookies = None,  # File in binary or hex
        user_id: str = None,
        passwd: str = None,
        email: str = None,
        email_passwd: str = None,
        callsign: str = None,
        ):
        error_message = ""
        try:
            # Authenticate the user
        
            # if authentication fails, auth function will return True and an error message
            user_db_key, admin_user = self.authenticate(
            id=user_id, passwd=passwd, key_db_pass=key_db_token, access_db=True
            )
        
            # In this case, user_db_key is used as an error code
            if user_db_key == True:
                # In this case, admin user is the error message
                return True, admin_user
            print(admin_user)

            # Connect to the database
            with securesql.connect(self.user_db_path) as user_db:
                user_db_cursor = user_db.cursor()
            
                # sqlite3 is weird so executescript must be used
                user_db_cursor.executescript(
                    f"""
                    PRAGMA key = '{user_db_key}';
                    PRAGMA cipher_compatibility = 3;
                    """
                )

                # callsign is the only value that can theoretically change in the users table
                # create a list of items that have been updated for JSON response
                updated =""
                if callsign != None: 
                    user_db_cursor.execute(
                        """
                        UPDATE users SET callsign=? WHERE user_id = ?
                
                        """,
                        (callsign, user_id)
                    )
                    updated += "callsign"

                login_query = "UPDATE users SET "
                login_params = []

                if email != None:
                    login_query += "email=?"
                    login_params.append(email)
                    updated += ", email"
                if email_passwd != None:
                    login_query += "email_passwd=?"
                    login_params.append(email_passwd)
                    updated += ", email password"
                if satnogs_cookies != None:
                    login_query += "satnogs_cookies=?"
                    login_params.append(satnogs_cookies)
                    updated += ", satnogs login cookies"

                # Update login data if needed
                if login_query != "UPDATE users SET ":
                    user_db_cursor.execute(login_query, login_params)

            # Create JSON response message
            message = "Successfully updated the following values: "+updated

            error = False
            return error, message
        except Exception as e:
             error_message = f"An error occurred: {e}"
             return True, error_message
        
    def listUsers(
        self,
        user_id: str,
        passwd: str,
        key_db_token: str,
    ):
        error_message = ""
        info = {
            'number_of_users': 0,
            'user_ids': []
            }

        try:
            user_db_key, admin_check = self.authenticate(
                id=user_id, passwd=passwd, key_db_pass=key_db_token, access_db=True
            )
            # In this case, user_db_key is used as an error code
            if user_db_key == True:
                # In this case, admin check is the error message
                return True, admin_check, {}
            print(user_db_key)
            if not admin_check:
                return True, "You must be an administrator to list users.", {}

            user_db = securesql.connect(self.user_db_path)
            user_db_cursor = user_db.cursor()

            # sqlite3 is weird so executescript must be used
            user_db_cursor.executescript(
                f"""
                PRAGMA key = '{user_db_key}';
                PRAGMA cipher_compatibility = 3;
                """
            )

            #if email_login or key_id or satnogs_cookies:
            user_db_cursor.execute(
                "SELECT user_id FROM users"
            )
            data = user_db_cursor.fetchall()

            if data:
                print(f"\n\n{data}")
                user_counter = 0
                user_ids = []
                for row in data:
                    print(row[0]) 
                    user_ids.append(row[0])
                    user_counter += 1
                info['user_ids'] = user_ids
                info["number_of_users"] = user_counter
     
            else:
                return True, "Database is corrupted", info
        
        except Exception as e:
            error_message = f"An error occurred: {e}"
            return True, error_message, info

        finally:
            if 'user_db' in locals():
                user_db.close()
        print(info)
        return False, error_message, info