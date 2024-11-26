import time
import os
import json
import bcrypt
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

    def __init__(self):
        self.user_db_key = str(token_hex(2048))  # Encryption key for user database
        self.key_db_token = str(token_hex(2048))  # Encryption key for key database
        print("Initialized secureSql instance.")

    def createUserDB(self):
        print("Creating user database...")
        self.user_db = securesql.connect(secureSql.user_db_path)
        self.user_db_cursor = self.user_db.cursor()

        # Generate admin credentials
        user_id = token_hex(16)
        raw_password = token_hex(256)  # Initial admin password
        passwd_hash = bcrypt.hashpw(raw_password.encode(), bcrypt.gensalt()).decode()  # Hash the password

        self.user_db_cursor.executescript(
            f"""
            PRAGMA key = '{self.user_db_key}';
            PRAGMA cipher_compatibility = 3;

            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                passwd_hash TEXT NOT NULL,
                is_admin INTEGER NOT NULL,
                callsign TEXT,
                creation_time INTEGER NOT NULL,
                key_id TEXT
            );

            CREATE TABLE IF NOT EXISTS logins (
                key_id TEXT PRIMARY KEY,
                email TEXT,
                email_passwd TEXT,
                satnogs_cookies TEXT 
            );
            """
        )
        # satnogs cookies are stored as base64 bytestring that has been converted into str
        # Insert admin user into the database
        self.user_db_cursor.execute(
            """
            INSERT INTO users (user_id, passwd_hash, is_admin, creation_time) 
            VALUES (?, ?, 1, ?)
            """,
            (user_id, passwd_hash, int(time.time())),
        )

        # Save admin credentials to a JSON file
        user_info = {
            'UserID': user_id,
            'Password': raw_password,  # Plain password saved only for first-time use
            'DBKey': self.key_db_token
        }
        with open(self.initial_userinfo_path, "w") as outfile:
            json.dump(user_info, outfile)
        print(f"Initial admin credentials saved to {self.initial_userinfo_path}")

        self.user_db.commit()
        print("User database created successfully.")

    def createKeyDB(self):
        print("Creating key database...")
        self.key_db = securesql.connect(self.key_db_path)
        self.key_db_cursor = self.key_db.cursor()

        creation_time = int(time.time())
        self.key_db_cursor.executescript(
            f"""
            PRAGMA key = '{self.key_db_token}';
            PRAGMA cipher_compatibility = 3;

            CREATE TABLE IF NOT EXISTS keys (
                user_db_key TEXT PRIMARY KEY,
                creation_time INTEGER NOT NULL
            );
            """
        )

        # Insert the user database encryption key into the keys table
        self.key_db_cursor.execute(
            "INSERT INTO keys (user_db_key, creation_time) VALUES (?, ?)",
            (self.user_db_key, creation_time)
        )
        print(f"Key database encryption token: {self.key_db_token}")

        self.key_db.commit()
        print("Key database created successfully.")

    def removeDB(self):
        print("Removing existing databases...")
        if os.path.exists(self.key_db_path):
            os.remove(self.key_db_path)
            print("Removed key database.")
        if os.path.exists(self.user_db_path):
            os.remove(self.user_db_path)
            print("Removed user database.")

    def migrate(self):
        print("Starting database migration...")
        self.removeDB()
        self.createUserDB()
        self.createKeyDB()
        print(
            f"Database migration complete.\n"
            f"Initial admin credentials are stored at {self.initial_userinfo_path}."
        )

    # Uncomment if necessary for cleaning up database connections
    """
    def __del__(self):
        if hasattr(self, 'user_db'):
            self.user_db.close()
        if hasattr(self, 'key_db'):
            self.key_db.close()
    """


if __name__ == "__main__":
    if input("Are you sure you want to delete the database and recreate it? (y/n): ").strip().lower() == "y":
        secureSql().migrate()
