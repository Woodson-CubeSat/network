from flask import Flask
from flask_restful import reqparse, Resource, abort
import requests
from time import time

from common.constants import USER_API_URL, GENERAL_API_URL, DB_KEY



parser = reqparse.RequestParser()


# Parameters for creating a new user
parser = reqparse.RequestParser()
parser.add_argument('Username', type=str, location='headers')
parser.add_argument('Password', type=str, location='headers')

# JWT
parser.add_argument('Authorization', type=str, location='headers')


# Keys that can be added
parser.add_argument('n2yo_key', type=str, location='form')
parser.add_argument('satnogs_key', type=str, location='form')


# # Options for fetching data (get) # I kept it here just in case I decide to add a function that fetches user information
# parser.add_argument('get_email_login', location='form')
# parser.add_argument('is_admin', location='form')
# parser.add_argument('get_callsign',  location='form')
# parser.add_argument('get_key_id', location='form')
# parser.add_argument('get_satnogs_cookies',  location='form')
# parser.add_argument('get_creation_time',  location='form')


# Options for creating a user (put)
parser.add_argument('username', type=str, location='form') # Also used to delete users
parser.add_argument('passwd', type=str, location='form')
parser.add_argument('email', type=str, location='form')
parser.add_argument('email_passwd', type=str, location='form')
parser.add_argument('satnogs_cookies', type=str, location='form')
parser.add_argument('callsign', type=str, location='form')
parser.add_argument('create_admin', location='form')


class ManageUsers(Resource):
    
    def get(self, action):
        args = parser.parse_args()
        if action == "auth" or action == "login" or action == "new_session" or action == "create_session":
            print("got here")
            auth_query = requests.get(url=USER_API_URL+"/create_session", headers={"UserID": args.Username, "Password": args.Password, "DBKey": DB_KEY})
            print(auth_query.json(), auth_query.status_code)
            return auth_query.json(), auth_query.status_code
        if action == "list_users":
            list_users_query = requests.get(url=USER_API_URL+'/list_users', headers={"Authorization": args.Authorization})
            return list_users_query.json(), list_users_query.status_code
        else:
            abort(405, description='Nonexsistent action or incorrect use case.')



    def put(self, action):
        args = parser.parse_args()
        # for creating a user
        print("action "+action)
        if action == 'create_user':
            print('create_admin', args.create_admin)
            print(args.username, args.passwd, args.satnogs_cookies, args.email, args.email_passwd, args.satnogs_key, args.n2yo_key)
            if args.username == None or args.passwd == None or args.satnogs_cookies == None or args.email == None or args.email_passwd == None or args.satnogs_key == None or args.n2yo_key == None:
                abort(405, description="Missing user  information.")
            create_user_query = requests.put(url=USER_API_URL+"/create_user", data={"username": args.username, "passwd": args.passwd, "email": args.email, "email_passwd": args.email_passwd, "satnogs_cookies": args.satnogs_cookies, "callsign": args.callsign, "create_admin": args.create_admin}, headers={"Authorization": args.Authorization})
            if create_user_query.status_code == 200:
                user_info = create_user_query.json()
                append_keys_query = requests.put(GENERAL_API_URL+'/append_keys', data={"key_id": user_info["key_id"], "n2yo_key": args.n2yo_key, "satnogs_key": args.satnogs_key})
                if append_keys_query.status_code == 200:
                    return user_info, create_user_query.status_code
                else:
                    # Delete user if keys cannot be appended
                    requests.delete(url=USER_API_URL+"/delete_user", data={'user_id': args.username}, headers={"Authorization": args.Authorization})
            else:
                return create_user_query.json(), create_user_query.status_code
        if action == 'update_user_info' or action == 'update_info':
            update_info_query = requests.put(url=USER_API_URL+"/update_info", data={"email": args.email, "email_passwd": args.email_passwd, "satnogs_cookies": args.satnogs_cookies, "callsign": args.callsign}, headers={"Authorization": args.Authorization}) 
            return update_info_query.json(), update_info_query.status_code
        else:
            abort(405, description="Nonexsistent action or incorrect use case.")


    def delete(self, action):
        print("hi")
        print(action)
        args = parser.parse_args()
        if action == 'delete_user':
            delete_user_query = requests.delete(url=USER_API_URL+"/delete_user", data={'user_id': args.username}, headers={"Authorization": args.Authorization})
            return delete_user_query.json(), delete_user_query.status_code
        else:
            abort(405, description='Nonexsistent action or incorrect use case.')

