from flask import Flask
from flask_restful import reqparse, Resource, abort
from common.handler import Sql, setupCronJob
from time import time
from common.handler import parseFrame, telemetryToZip
from common.constants import base_url


# will end up basing webserver off of test.py requests and processing


# get_struct = {'key_id': fields.String,
#             'is_admin': fields.Boolean,
#             'callsign': fields.String,
#             'creation_time': fields.Float, # will be transmitted as unix time
#             'satnogs_cookies' : fields.String, # will be transmitted as str and converted to binary object on webserver side (for seeding db)
#             'email_login': fields.Nested({
#                 'email': fields.String,
#                 'email_passwd': fields.String
#                 })
#             }

# put_struct = {'UserID': fields.String,
#               'Password': fields.String,
#               'key_id': fields.String}

parser = reqparse.RequestParser()



# options for data (put)

# filters for query
parser.add_argument('norad_id', type=int, location='form')
parser.add_argument('name', type=str, location='form')
parser.add_argument('country', type=str, location='form')
# filters for returning information
parser.add_argument('return_all', type=bool, location='form')
parser.add_argument('return_launchinfo', type=bool, location='form')
parser.add_argument('return_name', type=bool, location='form')
parser.add_argument('return_id', type=bool, location='form')
parser.add_argument('return_description', type=bool, location='form')


# options for data (put)

parser.add_argument('norad_id', type=int, location='form') # This argument will also be used as a filter for fetching telemetry, and deleting satellites
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


# options for data (delete)
parser.add_argument('user_id', type=str, location='form')

class ManageDB(Resource):
    
    def get(self, action):
        args = parser.parse_args()
        if action == 'get_satellite_info':  
            print(type(args.get_satnogs_cookies))
            error, message, info = Sql().getSatInfo(norad_id=args.norad_id, name=args.name, country=args.country, return_all=args.return_all, return_launchinfo=args.return_launchinfo, return_name=args.return_name, return_id=args.return_id, return_description=args.return_description)
            print(error)
            print(message)
            print(info)
            # If there is an error, the value for the error variable will be True
            if error:
                print("error")
                abort(500, message=message)
            if not error:
                return info
        if action == "get_telemetry":
            error, error_message, info = Sql().getTelemetry(norad_id=args.norad_id, start_time=args.start_time, end_time=args.end_time, station=args.station, return_metadata=args.return_metadata)
            if error:
                print("error")
                abort(500, message=error_message)
            if not error:
                if len(info) == 0:
                    return {'message': 'No data was returned for your query.'}
                    
                error, info = parseFrame(norad_id=args.norad_id, telemetry=info, decode_frames=args.decode_frames)
                if error:
                    return {'message': 'An error occured while parsing your frames'}
                if len(info) > 100:
                    # Generate the zip file
                    telemetry_file = telemetryToZip(args.norad_id, info)

                    # Construct the full URL
                    full_url = f"{base_url}/download_telemetry/{telemetry_file}"

                    # Return the full download URL
                    return {'message': 'The number of frames you requested exceeded the API limit. Please download your frames from the link provided.', 'download_url': full_url}
                else:
                    return info
        else:
            abort(405, message='Nonexsistent action or incorrect use case.')


    def put(self, action):
        args = parser.parse_args()
        # for creating a user
        print("action "+action)
        if action == 'append_telemetry': # only for ground station access, deal with it later
            error = True
            if error:
                print("error")
                abort(500, message="This function is not yet available.")
            if not error:
                pass
                # return info
        if action == 'add_satellite': 
            start_timestamp = time()
            if len(str(args.norad_id)) != 5:
                abort(405, message="Bad NORAD ID.")
            if args.key_id == None:
                abort(405, message="Bad key ID.")
            print(args.norad_id)
            error, message, info = Sql().buildTelemetry(norad_id=args.norad_id, satnogs_cookies=args.satnogs_cookies, email=args.email, email_passwd=args.email_passwd)
            if error:
                abort(500, message=message)
            if not error:
                info['time_taken'] -= start_timestamp
                satnogs_key= Sql().getKey(key_id=args.key_id, satnogs_key=True)
                print(satnogs_key)

                error, message = Sql().buildSatInfo(norad_id=args.norad_id, satnogs_key=satnogs_key, description=args.description, launch_date=args.launch_date, deployment_date=args.deployment_date)
                if error:
                    abort(500, message=message)
                if not error:
                    setupCronJob(key_id=args.key_id, norad_id=args.norad_id)
                    return {'message': message, 'appended': info}
            setupCronJob(key_id=args.key_id, norad_id=args.norad_id)
        if action == 'append_keys':
            if args.key_id == None or args.n2yo_key == None or args.satnogs_key == None:
                abort(400, message="Must include all required parameters.")
            else:
                error, message = Sql().appendKeys(key_id=args.key_id, n2yo_key=args.n2yo_key, satnogs_key=args.satnogs_key)
                if error:
                    abort(500, message=message)
                if not error:
                    {'message': message}
        # webserver should authenticate and make sure user is an admin first
        if action == 'add_ground_station':
            if args.name == None or args.lat == None or args.lng == None or args.alt == None or args.can_transmit == None or args.is_satnogs == None:
                abort(405, message="Missing ground station information.")
            else:
                error, message = Sql().addGroundstation(name=args.name, lat=args.lat, lng=args.lng, alt=args.alt, transmit=args.can_transmit, satnogs=args.is_satnogs)
                if error:
                    abort(500, message=message)
                if not error:
                    return {'message': message}
        
        else:
            abort(405, message="Nonexsistent action or incorrect use case.")


    def delete(self, action):
        print("hi")
        print(action)
        if action != 'delete_satellite':
            abort(405, message='Nonexsistent action or incorrect use case.')
        args = parser.parse_args()
        error, message = Sql().deleteSatellite(norad_id=args.norad_id)
        if not error:
            return {'message': message}
        else:
            abort(401, message=message)

