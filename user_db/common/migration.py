import time
import os
import json
from pysqlcipher3 import dbapi2 as securesql
from constants import script_dir
from secrets import token_hex


print(script_dir)

class secureSql:
    db_folder = "data"
    utilities_dir = "common"
    key_db_name = "keys"
    user_db_name = "private"
    key_db_path = f"{script_dir}/{utilities_dir}/{db_folder}/{key_db_name}.db"
    user_db_path = f"{script_dir}/{utilities_dir}/{db_folder}/{user_db_name}.db"
    initial_userinfo_path = f"{script_dir}/admin_info.json"
    print(user_db_path)

    def __init__(self):
        self.user_db_key = str(token_hex(2048))
        self.key_db_token = str(token_hex(2048))
        print("init")

    def createUserDB(self):
        print("got to createuserdb")
        print(secureSql.user_db_path)
        self.user_db = securesql.connect(secureSql.user_db_path)
        self.user_db_cursor = self.user_db.cursor()
        user_id = token_hex(16)
        passwd_hash = token_hex(1024)
        self.user_db_cursor.executescript(  
            f"""
            PRAGMA key = '{self.user_db_key}';

            PRAGMA cipher_compatibility = 3;

            create table if not exists users  (
                user_id str,
                passwd_hash str,
                is_admin int,
                callsign str,
                creation_time str,
                config_id str
            );

            create table if not exists vars (
                config_id int,
                email str,
                email_passwd str,
                satnogs_cookie blob
            )
            
            """
        )

        self.user_db_cursor.execute(
            f"""
            insert into users (user_id, passwd_hash, creation_time, is_admin) values (?,?,?,1)
            """, (user_id,passwd_hash,int(time.time()))
        )


        user_info = {
            'UserID': user_id,
            'Password': passwd_hash,
            'DBKey': self.key_db_token
        }
        with open(self.initial_userinfo_path, "w") as outfile:
            json.dump(user_info, outfile)
        self.user_db.commit()
        print("created user db")

    def createKeyDB(self):
        self.key_db = securesql.connect(self.key_db_path)
        self.key_db_cursor = self.key_db.cursor()
        creation_time = int(time.time())
        self.key_db_cursor.executescript(  
            f"""
            PRAGMA key = '{self.key_db_token}';

            PRAGMA cipher_compatibility = 3;

            create table if not exists keys  (
                user_db_key str,
                creation_time int
            );

            """
        )

        self.key_db_cursor.execute("""insert into keys (user_db_key, creation_time) values (?, ?)""", (self.user_db_key, creation_time))
        self.key_db_cursor.execute("""select user_db_key from keys""")
        print("key db token\n\n\n"+self.key_db_token)
        data = self.key_db_cursor.fetchall()
        print(data[0])
        self.key_db.commit()

    def removeDB(self):
        if os.path.exists(self.key_db_path):
            os.remove(self.key_db_path)
            print("removing key db")
        if os.path.exists(self.user_db_path):
            os.remove(self.user_db_path)
            print("removing user db")
  
    def migrate(self):
        self.removeDB()
        self.createUserDB()
        self.createKeyDB()
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou can find the user credetials for the initial admin user at {self.initial_userinfo_path}")


"""
    def __del__(self):
        self.user_db.close()
        self.key_db.close()

"""
if __name__ == "__main__":
    #if input("Are you sure you want to delete the database and recreate it? (y/n) ").strip() == "y":
    secureSql().migrate()
# Checklist

# fix SQL get and append
# change DBCheck and update_frames to work with new DB system
# HI POOKIE DOOKIE BOOKIE BEAR
