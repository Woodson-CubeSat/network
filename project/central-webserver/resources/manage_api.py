from flask import Flask
from flask_restful import reqparse, Resource, abort
import requests
from time import time

from common.constants import USER_API_URL, GENERAL_API_URL, DB_KEY



parser = reqparse.RequestParser()


# Parameters for creating a new
parser = reqparse.RequestParser()

# JWT
parser.add_argument('Authorization', type=str, location='headers')


# filters for satellite info query
parser.add_argument('name', type=str, location='form')
parser.add_argument('country', type=str, location='form')
# filters for returning information
parser.add_argument('return_all', location='form')
parser.add_argument('return_launchinfo', location='form')
parser.add_argument('return_name', location='form')
parser.add_argument('return_id', location='form')
parser.add_argument('return_description', location='form')


# options for data (put)

parser.add_argument('norad_id', type=int, location='form') # This argument will also be used as a filter for fetching telemetry, getting satellite info, and deleting satellites
parser.add_argument('description', type=str, location='form')
parser.add_argument('launch_date', type=str, location='form')
parser.add_argument('deployment_date', type=str, location='form')

# Parameters for adding a ground station
parser.add_argument('name', type=str, location='form')
parser.add_argument('lat', type=str, location='form')
parser.add_argument('lng', type=str, location='form')
parser.add_argument('alt', type=str, location='form')
parser.add_argument('can_transmit', location='form')
parser.add_argument('is_satnogs', location='form')
# Parameters for telemetry retrieval
parser.add_argument('start_time', type=int, location='form')
parser.add_argument('end_time', type=int, location='form')
parser.add_argument('station', type=str, location='form')
parser.add_argument('return_metadata', location='form', default=False)
parser.add_argument('decode_frames', location='form', default=False)


class ManageData(Resource):
    
    def get(self, action):
        args = parser.parse_args()
        if action == 'get_satellite_info':  
            auth_query = requests.get(url=USER_API_URL+"/jwt", headers={"Authorization": args.Authorization})
            if auth_query.status_code == 200:
                print(auth_query.json()["user_id"])
                print(auth_query.json()["admin_status"])
                get_sat_info_query = requests.get(url=GENERAL_API_URL+'/get_satellite_info', data={'norad_id': args.norad_id, 'name': args.name, 'country': args.country, 'return_all': args.return_all, 'return_launchinfo': args.return_launchinfo, 'return_name': args.return_name, 'return_id': args.return_id, 'return_description': args.return_description})
                return get_sat_info_query.json(), get_sat_info_query.status_code
            else:
                abort(auth_query.status_code, description="Authentication failed.")
        if action == "get_telemetry":
            auth_query = requests.get(url=USER_API_URL+"/jwt", headers={"Authorization": args.Authorization})
            if auth_query.status_code == 200:
                print(auth_query.json()["user_id"])
                print(auth_query.json()["admin_status"])
                telemetry_query = requests.get(url=GENERAL_API_URL+'/get_telemetry', data={'norad_id': args.norad_id, 'start_time': args.start_time, 'end_time': args.end_time, 'station': args.station, 'return_metadata': args.return_metadata, 'decode_frames': args.decode_frames})                
                return telemetry_query.json(), telemetry_query.status_code
            else:
                abort(auth_query.status_code, description="Authentication failed.")
        if action == "list_ground_stations":
            auth_query = requests.get(url=USER_API_URL+"/jwt", headers={"Authorization": args.Authorization})
            if auth_query.status_code == 200:
                print('is_admin', type(auth_query.json()["admin_status"]))
                if auth_query.json()["admin_status"] == True:
                    ground_station_query = requests.get(url=GENERAL_API_URL+'/list_ground_stations')                
                    return ground_station_query.json(), ground_station_query.status_code
                else:
                    abort(403, description="You must be an administrator to add a satellite to the database.")
            else:
                abort(auth_query.status_code, description="Authentication failed.")
    
        else:
            abort(405, description='Nonexsistent action or incorrect use case.')



    def put(self, action):
        args = parser.parse_args()
        # for creating a user
        print("action "+action)
        if action == 'append_telemetry': # only for ground station access, deal with it later
            abort(500, description="This function is not yet available.")
        if action == 'add_satellite': 
            if args.norad_id == None:
                abort(405, description="Missing NORAD ID.")
            get_info_query = requests.get(url=USER_API_URL+'/get_info', data={'get_email_login': True, 'is_admin': True, 'get_key_id': True, 'get_satnogs_cookies': True}, headers={"Authorization": args.Authorization})
            print('query:', get_info_query.json())
            if get_info_query.status_code == 200:
                print('is_admin', type(get_info_query.json()["is_admin"]))
                try:
                    print('key_id', get_info_query.json()['key_id'])
                except:
                    abort(500, description="Your data is corrupted, and the server cannot fetch your data configuration.")
                if get_info_query.json()["is_admin"] == True:
                    user_info = get_info_query.json()
                    add_satellite_query = requests.put(url=GENERAL_API_URL+'/add_satellite', data={'norad_id': args.norad_id, 'email': user_info['email_login']['email'], 'email_passwd': user_info['email_login']['email_passwd'], 'satnogs_cookies': user_info['satnogs_cookies'], 'key_id': user_info['key_id']})  
                    return add_satellite_query.json(), add_satellite_query.status_code
                else:
                    abort(403, description="You must be an administrator to add a satellite to the database.")
            else:
                abort(get_info_query.status_code, description="Authentication failed.")
        # webserver should authenticate and make sure user is an admin first
        if action == 'add_ground_station':
            if args.name == None or args.lat == None or args.lng == None or args.alt == None or args.can_transmit == None or args.is_satnogs == None:
                abort(405, description="Missing ground station information.")
            auth_query = requests.get(url=USER_API_URL+"/jwt", headers={"Authorization": args.Authorization})
            if auth_query.status_code == 200:
                print(auth_query.json()["user_id"])
                print(auth_query.json()["admin_status"])
                if auth_query.json()["admin_status"] == True:
                        add_station_query = requests.put(url=GENERAL_API_URL+'/add_ground_station', data={'name': args.name, 'lat': args.lat, 'lng': args.lng, 'alt': args.alt, 'can_transmit': args.can_transmit, 'is_satnogs': args.is_satnogs})  
                        return add_station_query.json(), 200
                else:
                    abort(403, description="You must be an administrator to add a ground station.")
        else:
            abort(405, description="Nonexsistent action or incorrect use case.")


    def delete(self, action):
        print("hi")
        print(action)
        args = parser.parse_args()
        if action == 'delete_satellite':
            auth_query = requests.get(url=USER_API_URL+"/jwt", headers={"Authorization": args.Authorization})
            if auth_query.status_code == 200:
                print(auth_query.json()["user_id"])
                print(auth_query.json()["admin_status"])
                if auth_query.json()["admin_status"] == True:
                        delete_sat_query = requests.delete(url=GENERAL_API_URL+'/delete_satellite', data={'norad_id': args.norad_id})  
                        return delete_sat_query.json(), delete_sat_query.status_code
                else:
                    abort(403, description="You must be an administrator to delete a satellite from the database.")
        else:
            abort(405, description='Nonexsistent action or incorrect use case.')

