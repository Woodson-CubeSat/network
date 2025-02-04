from secrets import token_hex
import time
from common.constants import script_dir
from pysqlcipher3 import dbapi2 as securesql
import bcrypt
from queue import Queue

class ConnectionPool:
    def __init__(self, db_path, pool_size=5):
        self.pool = Queue(maxsize=pool_size)
        print(f"Initializing connection pool with db_path={db_path}")
        for i in range(pool_size):
            try:
                conn = securesql.connect(db_path, check_same_thread=False)
                self.pool.put(conn)
                print(f"Connection {i+1}/{pool_size} added to pool")
            except Exception as e:
                print(f"Error creating connection {i+1}: {e}")

    def get_connection(self, timeout=5):
        try:
            print("Attempting to get connection from pool with timeout")
            conn = self.pool.get(timeout=timeout)
            print(f"Connection acquired: {conn}")
            return conn
        except Exception as e:
            print(f"Error getting connection: {e}")
            raise

    def release_connection(self, conn):
        print(f"Releasing connection: {conn}")
        try:
            if self.pool.full():
                print("Connection pool is full, discarding connection.")
                conn.close()  # Discard the connection
                return
            self.pool.put(conn, timeout=2)  # Use timeout to detect blocking
            print(f"Connection released back to pool: {conn}")
        except Exception as e:
            print(f"Error releasing connection: {e}")

    def close_all(self):
        print("Closing all connections in the pool")
        while not self.pool.empty():
            conn = self.pool.get()
            try:
                conn.close()
                print(f"Connection closed: {conn}")
            except Exception as e:
                print(f"Error closing connection: {e}")


class SecureSql:
    def __init__(self, pool_size=5):
        db_folder = "data"
        utilities_dir = "common"
        key_db_name = "keys"
        user_db_name = "private"
        self.key_db_path = f"{script_dir}/{utilities_dir}/{db_folder}/{key_db_name}.db"
        self.user_db_path = f"{script_dir}/{utilities_dir}/{db_folder}/{user_db_name}.db"
        
        # Initialize connection pools
        self.key_db_pool = ConnectionPool(self.key_db_path, pool_size)
        self.user_db_pool = ConnectionPool(self.user_db_path, pool_size)
        print("got here X2")

    def authenticate(self, id: str, passwd: str, key_db_pass: str):
        key_conn = self.key_db_pool.get_connection()
        key_cursor = key_conn.cursor()

        try:
            key_cursor.executescript(f"""
                PRAGMA key = '{key_db_pass}';
                PRAGMA cipher_compatibility = 3;
            """)

            key_cursor.execute("SELECT user_db_key FROM keys")
            user_db_key = key_cursor.fetchone()[0]
            self.key_db_pool.release_connection(key_conn)

            user_conn = self.user_db_pool.get_connection()
            user_cursor = user_conn.cursor()
            user_cursor.executescript(f"""
                PRAGMA key = '{user_db_key}';
                PRAGMA cipher_compatibility = 3;
            """)
            user_cursor.execute(
                "SELECT passwd_hash, is_admin FROM users WHERE user_id = ?",
                (id,)
            )
            user_data = user_cursor.fetchone()

            if not user_data:
                return True, False, "Invalid username."

            stored_hash, is_admin = user_data
            if not bcrypt.checkpw(passwd.encode(), stored_hash.encode()):
                return True, False, "Invalid password."

            print("got here X3", print(is_admin))
            return False, bool(is_admin), ""

        except Exception as e:
            return True, f"Authentication error: {e}"
        finally:
            if key_conn:
                try:
                    self.key_db_pool.release_connection(key_conn)
                    key_conn = None  # Avoid double release
                except Exception as e:
                    print(f"Error releasing key_conn: {e}")

            if user_conn:
                try:
                    self.user_db_pool.release_connection(user_conn)
                    user_conn = None  # Avoid double release
                except Exception as e:
                    print(f"Error releasing user_conn: {e}")

        # finally:
        #     self.key_db_pool.release_connection(key_conn)
        #     if 'user_conn' in locals():
        #         self.user_db_pool.release_connection(user_conn)

    def getUserDBKey(self, key_db_pass: str):
        key_conn = self.key_db_pool.get_connection()
        key_cursor = key_conn.cursor()

        try:
            key_cursor.executescript(f"""
                PRAGMA key = '{key_db_pass}';
                PRAGMA cipher_compatibility = 3;
            """)

            key_cursor.execute("SELECT user_db_key FROM keys")
            user_db_key = key_cursor.fetchone()[0]
            return False, user_db_key

        except Exception as e:
            return True, f"Authentication error: {e}"

        finally:
            self.key_db_pool.release_connection(key_conn)

    def getUserInfo(self, key_db_token: str, user_id: str, sudo: bool, **kwargs):
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
            error, user_db_key = self.getUserDBKey(key_db_pass=key_db_token)
            if error:
                return True, user_db_key

            user_conn = self.user_db_pool.get_connection()
            user_cursor = user_conn.cursor()
            user_cursor.executescript(f"""
                PRAGMA key = '{user_db_key}';
                PRAGMA cipher_compatibility = 3;
            """)

            print('key_id parameter', kwargs.get('key_id'))
            if kwargs.get('email_login') or kwargs.get('key_id') or kwargs.get('satnogs_cookies'):
                user_cursor.execute(
                    "SELECT key_id FROM users WHERE user_id=?", (user_id,)
                )
                data = user_cursor.fetchall()
                print('data for key id', data)
                if data:
                    info["key_id"] = data[0][0]
                    config_id = data[0][0]
                else:
                    return True, "No matching user found.", info

                if kwargs.get('email_login'):
                    user_cursor.execute("SELECT email, email_passwd FROM logins WHERE key_id=?", (config_id,))
                    data = user_cursor.fetchall()
                    if data:
                        info["email_login"]["email"], info["email_login"]["email_passwd"] = data[0]

                if kwargs.get('satnogs_cookies'):
                    user_cursor.execute("SELECT satnogs_cookies FROM logins WHERE key_id=?", (config_id,))
                    data = user_cursor.fetchone()
                    info["satnogs_cookies"] = data[0] if data else None

            if kwargs.get('is_admin'):
                info["is_admin"] = sudo

            if kwargs.get('callsign'):
                user_cursor.execute("SELECT callsign FROM users WHERE user_id=?", (user_id,))
                info["callsign"] = user_cursor.fetchone()[0]

            if kwargs.get('creation_time'):
                user_cursor.execute("SELECT creation_time FROM users WHERE user_id=?", (user_id,))
                info["creation_time"] = user_cursor.fetchone()[0]

            print(info)
            return False, "", info



        except Exception as e:
            return True, f"An error occurred: {e}", info

        finally:
            self.user_db_pool.release_connection(user_conn)

    def buildUserInfo(self, sudo: bool, username: str, passwd: str, satnogs_cookies, key_db_token: str, email: str, email_passwd: str, callsign: str = None, create_admin: bool = False):
        try:
            error, user_db_key = self.getUserDBKey(key_db_pass=key_db_token)
            if error:
                return True, user_db_key, {}

            if not sudo:
                return True, "Must be an administrator to create users.", {}

            user_conn = self.user_db_pool.get_connection()
            user_cursor = user_conn.cursor()
            user_cursor.executescript(f"""
                PRAGMA key = '{user_db_key}';
                PRAGMA cipher_compatibility = 3;
            """)

            user_cursor.execute("SELECT COUNT(*) FROM users WHERE user_id = ?", (username,))
            if user_cursor.fetchone()[0] > 0:
                return True, f"User '{username}' already exists.", {}

            key_id = token_hex(16)
            passwd_hash = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt()).decode()
            user_cursor.execute(
                """
                INSERT INTO users (user_id, passwd_hash, is_admin, callsign, creation_time, key_id)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (username, passwd_hash, int(create_admin), callsign, time.time(), key_id)
            )

            user_cursor.execute(
                """
                INSERT INTO logins (key_id, email, email_passwd, satnogs_cookies)
                VALUES (?, ?, ?, ?)
                """, (key_id, email, email_passwd, satnogs_cookies)
            )
            user_conn.commit()

            return False, "", {'username': username, 'key_id': key_id, 'description': 'User added successfully.'}

        except Exception as e:
            return True, f"An error occurred: {e}", {}

        finally:
            self.user_db_pool.release_connection(user_conn)

    def deleteUser(self, sudo: bool, key_db_token: str, user_id: str):
        try:
            error, user_db_key = self.getUserDBKey(key_db_pass=key_db_token)
            if error:
                return True, user_db_key, {}

            if not sudo:
                return True, "Must be an administrator to delete users.", {}

            user_conn = self.user_db_pool.get_connection()
            user_cursor = user_conn.cursor()
            user_cursor.executescript(f"""
                PRAGMA key = '{user_db_key}';
                PRAGMA cipher_compatibility = 3;
            """)

            user_cursor.execute("SELECT key_id FROM users WHERE user_id=?", (user_id,))
            data = user_cursor.fetchone()
            if not data:
                return True, "User does not exist.", {}

            key_id = data[0]
            user_cursor.execute("DELETE FROM users WHERE user_id=?", (user_id,))
            user_cursor.execute("DELETE FROM logins WHERE key_id=?", (key_id,))
            user_conn.commit()

            return False, ""

        except Exception as e:
            return True, f"An error occurred: {e}"

        finally:
            self.user_db_pool.release_connection(user_conn)

    def updateUserInfo(self, key_db_token: str, user_id: str, **kwargs):
        try:
            error, user_db_key = self.getUserDBKey(key_db_pass=key_db_token)
            if error:
                return True, user_db_key

            user_conn = self.user_db_pool.get_connection()
            user_cursor = user_conn.cursor()
            user_cursor.executescript(f"""
                PRAGMA key = '{user_db_key}';
                PRAGMA cipher_compatibility = 3;
            """)

            updated = []
            if 'callsign' in kwargs:
                user_cursor.execute("UPDATE users SET callsign=? WHERE user_id=?", (kwargs['callsign'], user_id))
                updated.append('callsign')

            login_query = []
            login_params = []
            if 'email' in kwargs:
                login_query.append("email=?")
                login_params.append(kwargs['email'])
            if 'email_passwd' in kwargs:
                login_query.append("email_passwd=?")
                login_params.append(kwargs['email_passwd'])
            if 'satnogs_cookies' in kwargs:
                login_query.append("satnogs_cookies=?")
                login_params.append(kwargs['satnogs_cookies'])

            if login_query:
                user_cursor.execute("SELECT key_id FROM users WHERE user_id=?", (user_id,))
                key_id = user_cursor.fetchone()[0]
                login_params.append(key_id)
                query = f"UPDATE logins SET {', '.join(login_query)} WHERE key_id=?"
                user_cursor.execute(query, login_params)
                updated.extend(login_query)

            user_conn.commit()
            return False, f"Successfully updated: {', '.join(updated)}"

        except Exception as e:
            return True, f"An error occurred: {e}"

        finally:
            self.user_db_pool.release_connection(user_conn)

    def listUsers(self, sudo: bool, key_db_token: str):
        try:
            error, user_db_key = self.getUserDBKey(key_db_pass=key_db_token)
            if error:
                return True, user_db_key, {}

            if not sudo:
                return True, "Must be an administrator to list users.", {}

            user_conn = self.user_db_pool.get_connection()
            user_cursor = user_conn.cursor()
            user_cursor.executescript(f"""
                PRAGMA key = '{user_db_key}';
                PRAGMA cipher_compatibility = 3;
            """)

            user_cursor.execute("SELECT user_id, is_admin FROM users")
            data = user_cursor.fetchall()
            return False, "", {'number_of_users': len(data), 'users': [{'username': row[0], 'admin': bool(row[1])} for row in data]}

        except Exception as e:
            return True, f"An error occurred: {e}", {}

        finally:
            self.user_db_pool.release_connection(user_conn)

    def close_pools(self):
        self.key_db_pool.close_all()
        self.user_db_pool.close_all()