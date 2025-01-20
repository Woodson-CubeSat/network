from flask import Flask
from flask_restful import reqparse, Resource, abort
import requests
from time import time

from common.constants import USER_API_URL, GENERAL_API_URL, DB_KEY



parser = reqparse.RequestParser()


# Parameters for creating a new
parser = reqparse.RequestParser()
parser.add_argument('Username', type=str, location='headers')
parser.add_argument('Password', type=str, location='headers')
parser.add_argument('DBKey', type=str, location='headers')

# JWT
parser.add_argument('Authentication', type=str, location='headers')

# General API Options start here

# options for data (put)

# filters for satellite info query
parser.add_argument('name', type=str, location='form')
parser.add_argument('country', type=str, location='form')
# filters for returning information
parser.add_argument('return_all', type=bool, location='form')
parser.add_argument('return_launchinfo', type=bool, location='form')
parser.add_argument('return_name', type=bool, location='form')
parser.add_argument('return_id', type=bool, location='form')
parser.add_argument('return_description', type=bool, location='form')


# options for data (put)

parser.add_argument('norad_id', type=int, location='form') # This argument will also be used as a filter for fetching telemetry, getting satellite info, and deleting satellites
parser.add_argument('description', type=str, location='form')
parser.add_argument('launch_date', type=str, location='form')
parser.add_argument('deployment_date', type=str, location='form')
# for creating the cron command and appending keys to db
parser.add_argument('key_id', type=str, location='form')
# these will be parameters passed by the webserver (which will retrive them from the user db api)
# these parameters will be used to scrape satellite telemetry
parser.add_argument('email', type=str, location='form')
parser.add_argument('email_passwd', type=str, location='form')
parser.add_argument('satnogs_cookies', type=str, location='form')
# Keys that can be added
parser.add_argument('n2yo_key', type=str, location='form')
parser.add_argument('satnogs_key', type=str, location='form')
# Parameters for adding a ground station
parser.add_argument('name', type=str, location='form')
parser.add_argument('lat', type=str, location='form')
parser.add_argument('lng', type=str, location='form')
parser.add_argument('alt', type=str, location='form')
parser.add_argument('can_transmit', type=bool, location='form')
parser.add_argument('is_satnogs', type=bool, location='form')
# Parameters for telemetry retrieval
parser.add_argument('start_time', type=int, location='form')
parser.add_argument('end_time', type=int, location='form')
parser.add_argument('station', type=str, location='form')
parser.add_argument('return_metadata', type=bool, location='form', default=False)
parser.add_argument('decode_frames', type=bool, location='form', default=False)





# User API options start here

# Options for data (get)
parser.add_argument('get_email_login', type=bool, location='form')
parser.add_argument('is_admin', type=bool, location='form')
parser.add_argument('get_callsign', type=bool, location='form')
parser.add_argument('get_key_id', type=bool, location='form')
parser.add_argument('get_satnogs_cookies', type=bool, location='form')
parser.add_argument('get_creation_time', type=bool, location='form')


# Options for data (put)
parser.add_argument('username', type=str, location='form') # Also used to delete users
parser.add_argument('passwd', type=str, location='form')
parser.add_argument('email', type=str, location='form')
parser.add_argument('email_passwd', type=str, location='form')
parser.add_argument('satnogs_cookies', type=str, location='form')
parser.add_argument('callsign', type=str, location='form')
parser.add_argument('create_admin', type=bool, location='form')

# Options for data (delete)
parser.add_argument('user_id', type=str, location='form')


class ManageAPI(Resource):
    
    def get(self, action):
        args = parser.parse_args()
        if action == 'get_satellite_info':  
            auth_query = requests.get(url=USER_API_URL+"/jwt", headers={"Authentication": args.Authentication})
            if auth_query.status_code == 200:
                print(auth_query.json()["user_id"])
                print(auth_query.json()["admin_status"])
                get_sat_info_query = requests.get(url=GENERAL_API_URL+'/get_satellite_info', data={'norad_id': args.norad_id, 'name': args.name, 'country': args.country, 'return_all': args.return_all, 'return_launchinfo': args.return_launchinfo, 'return_name': args.return_name, 'return_id': args.return_id, 'return_description': args.return_description})
                return get_sat_info_query.json(), get_sat_info_query.status_code
            else:
                abort(auth_query.status_code, message="Authentication failed")
        if action == "get_telemetry":
            auth_query = requests.get(url=USER_API_URL+"/jwt", headers={"Authentication": args.Authentication})
            if auth_query.status_code == 200:
                print(auth_query.json()["user_id"])
                print(auth_query.json()["admin_status"])
                telemetry_query = requests.get(url=GENERAL_API_URL+'/get_telemetry', data={'norad_id': args.norad_id, 'start_time': args.start_time, 'end_time': args.end_time, 'station': args.station, 'return_metadata': args.return_metadata, 'decode_frames': args.decode_frames})                
                return telemetry_query.json(), telemetry_query.status_code
            else:
                abort(auth_query.status_code, message="Authentication failed")
        if action == "auth" or action == "login" or action == "new_session":
            auth_query = requests.get(url=USER_API_URL+"/create_session", headers={"UserID": args.Username, "Password": args.Password, "DBKey": DB_KEY})
            return auth_query.json(), auth_query.status_code
        if action == "list_users":
            list_users_query = requests.get(url=USER_API_URL+'/list_users', headers={"Authentication": args.Authentication})
            return list_users_query.json(), list_users_query.status_code
        else:
            abort(405, message='Nonexsistent action or incorrect use case.')



    def put(self, action):
        args = parser.parse_args()
        # for creating a user
        print("action "+action)
        if action == 'append_telemetry': # only for ground station access, deal with it later
            abort(500, message="This function is not yet available.")
        if action == 'add_satellite': 
            if args.norad_id == None:
                abort(405, message="Missing NORAD ID.")
            get_info_query = requests.get(url=USER_API_URL+'/get_info', data={'get_email_login': True, 'is_admin': True, 'get_key_id': True, 'get_satnogs_cookies': True}, headers={"Authentication": args.Authentication})
            if get_info_query.status_code == 200:
                print(get_info_query.json()["is_admin"])
                if get_info_query.json()["is_admin"] == True:
                    user_info = get_info_query.json()
                    add_satellite_query = requests.put(url=GENERAL_API_URL+'/add_satellite', data={'norad_id': args.norad_id, 'email': user_info['email_login']['email'], 'email_passwd': user_info['email_login']['email_passwd'], 'satnogs_cookies': user_info['satnogs_cookies']})  
                    return add_satellite_query.json(), add_satellite_query.status_code
                else:
                    abort(403, message="You must be an administrator to delete a satellite from the database.")
            else:
                abort(get_info_query.status_code, message="Authentication failed")
            get_info_query = requests.get(url=USER_API_URL+'/get_info', data={"get": True}, headers={"Authentication": args.Authentication})
        if action == 'create_user':
            if args.username == None or args.passwd == None or args.satnogs_cookies == None or args.email == None or args.email_passwd == None or args.satnogs_key == None or args.n2yo_key == None:
                abort(405, message="Missing user  information.")
            create_user_query = requests.put(url=USER_API_URL+"/create_user", data={"username": args.username, "passwd": args.passwd, "email": args.email, "email_passwd": args.email_passwd, "satnogs_cookies": args.satnogs_cookies, "callsign": args.callsign, "create_admin": args.create_admin}, headers={"Authentication": args.Authentication})
            if create_user_query.status_code == 200:
                user_info = create_user_query.json()
                append_keys_query = requests.put(GENERAL_API_URL+'/append_keys', data={"key_id": user_info["key_id"], "n2yo_key": args.n2yo_key, "satnogs_key": args.satnogs_key})
                if append_keys_query.status_code == 200:
                    return user_info, create_user_query.status_code
                else:
                    # Delete user if keys cannot be appended
                    requests.delete(url=USER_API_URL+"/delete_user", data={'user_id': args.username}, headers={"Authentication": args.Authentication})
            else:
                return create_user_query.json(), create_user_query.status_code
        # webserver should authenticate and make sure user is an admin first
        if action == 'add_ground_station':
            if args.name == None or args.lat == None or args.lng == None or args.alt == None or args.can_transmit == None or args.is_satnogs == None:
                abort(405, message="Missing ground station information.")
            auth_query = requests.get(url=USER_API_URL+"/jwt", headers={"Authentication": args.Authentication})
            if auth_query.status_code == 200:
                print(auth_query.json()["user_id"])
                print(auth_query.json()["admin_status"])
                if auth_query.json()["admin_status"] == True:
                        add_station_query = requests.put(url=GENERAL_API_URL+'/add_ground_station', data={'name': args.name, 'lat': args.lat, 'lng': args.lng, 'alt': args.alt, 'can_transmit': args.can_transmit, 'is_satnogs': args.is_satnogs})  
                        return add_station_query.json(), 200
                else:
                    abort(403, message="You must be an administrator to add a ground station.")

        if action == 'update_user_info':
            update_info_query = requests.put(url=USER_API_URL+"/create_user", data={"email": args.email, "email_passwd": args.email_passwd, "satnogs_cookies": args.satnogs_cookies, "callsign": args.callsign}, headers={"Authentication": args.Authentication}) 
            return update_info_query.json(), update_info_query.status_code
        else:
            abort(405, message="Nonexsistent action or incorrect use case.")


    def delete(self, action):
        print("hi")
        print(action)
        args = parser.parse_args()
        if action == 'delete_satellite':
            auth_query = requests.get(url=USER_API_URL+"/jwt", headers={"Authentication": args.Authentication})
            if auth_query.status_code == 200:
                print(auth_query.json()["user_id"])
                print(auth_query.json()["admin_status"])
                if auth_query.json()["admin_status"] == True:
                        delete_sat_query = requests.delete(url=GENERAL_API_URL+'/delete_satellite', data={'norad_id': args.norad_id})  
                        return delete_sat_query.json(), delete_sat_query.status_code
                else:
                    abort(403, message="You must be an administrator to delete a satellite from the database.")

        if action == 'delete_user':
            delete_user_query = requests.delete(url=USER_API_URL+"/delete_user", data={'user_id': args.username}, headers={"Authentication": args.Authentication})
            return delete_user_query.json(), delete_user_query.status_code
        else:
            abort(405, message='Nonexsistent action or incorrect use case.')

