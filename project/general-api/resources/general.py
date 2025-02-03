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
parser.add_argument('return_all', location='form')
parser.add_argument('return_launchinfo', location='form')
parser.add_argument('return_name', location='form')
parser.add_argument('return_id', location='form')
parser.add_argument('return_description', location='form')


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
parser.add_argument('can_transmit', location='form')
parser.add_argument('is_satnogs', location='form')
# Parameters for telemetry retrieval
parser.add_argument('start_time', type=int, location='form')
parser.add_argument('end_time', type=int, location='form')
parser.add_argument('station', type=str, location='form')
parser.add_argument('return_metadata', location='form', default=False)
parser.add_argument('decode_frames', location='form', default=False)


# options for data (delete)
parser.add_argument('user_id', type=str, location='form')

class ManageDB(Resource):
    
    def get(self, action):
        args = parser.parse_args()
        if action == 'get_satellite_info':  
            boolean_fields = [
                'return_all', 
                'return_launchinfo', 
                'return_name', 
                'return_id', 
                'return_description'
            ]
            
            dynamic_variables = {}
            # Dynamically create standalone variables
            for field in boolean_fields:
                print(field)
                value = args.get(field)  # Get the value of the argument
                print('value', value)
                # Convert "True" or "False" strings to actual booleans or None
                converted_value = value == "True" if value is not None else False
                dynamic_variables[field] = converted_value

            error, message, info = Sql().getSatInfo(norad_id=args.norad_id, name=args.name, country=args.country, return_all=dynamic_variables["return_all"], return_launchinfo=dynamic_variables["return_launchinfo"], return_name=dynamic_variables["return_name"], return_id=dynamic_variables["return_id"], return_description=dynamic_variables["return_description"])
            print(error)
            print(message)
            # If there is an error, the value for the error variable will be True
            if error:
                print("error")
                abort(500, description=message)
            if not error:
                return info
        if action == "get_telemetry":
            error, error_message, info = Sql().getTelemetry(norad_id=args.norad_id, start_time=args.start_time, end_time=args.end_time, station=args.station, return_metadata=args.return_metadata)
            if error:
                print("error")
                abort(500, description=error_message)
            if not error:
                if len(info) == 0:
                    return {'description': 'No data was returned for your query.'}
                    
                error, info = parseFrame(norad_id=args.norad_id, telemetry=info, decode_frames=args.decode_frames)
                if error:
                    return {'description': 'An error occured while parsing your frames'}
                if len(info) > 100:
                    # Generate the zip file
                    telemetry_file = telemetryToZip(args.norad_id, info)

                    # Construct the full URL
                    full_url = f"{base_url}/download_telemetry/{telemetry_file}"

                    # Return the full download URL
                    return {'description': 'The number of frames you requested exceeded the API limit. Please download your frames from the link provided.', 'download_url': full_url}
                else:
                    return info
        if action == "list_ground_stations":
            error, message, info = Sql().listGroundStations()
            if error:
                abort(500, description=message)
            return info, 200
        else:
            abort(405, description='Nonexsistent action or incorrect use case.')


    def put(self, action):
        args = parser.parse_args()
        # for creating a user
        print("action "+action)
        if action == 'append_telemetry': # only for ground station access, deal with it later
            error = True
            if error:
                print("error")
                abort(500, description="This function is not yet available.")
            if not error:
                pass
                # return info
        if action == 'add_satellite': 
            start_timestamp = time()
            if len(str(args.norad_id)) != 5:
                abort(405, description="Bad NORAD ID.")
            if args.key_id == None:
                abort(405, description="Bad key ID.")
            print(args.norad_id)
            sql = Sql()
            error, message, info = sql.buildTelemetry(norad_id=args.norad_id, satnogs_cookies=args.satnogs_cookies, email=args.email, email_passwd=args.email_passwd)
            if error:
                abort(500, description=message)
            if not error:
                info['time_taken'] -= start_timestamp
                satnogs_key= sql.getKey(key_id=args.key_id, satnogs_key=True)
                print(satnogs_key)

                error, message = sql.buildSatInfo(norad_id=args.norad_id, satnogs_key=satnogs_key, description=args.description, launch_date=args.launch_date, deployment_date=args.deployment_date)
                if error:
                    abort(500, description=message)
                if not error:
                    setupCronJob(key_id=args.key_id, norad_id=args.norad_id)
                    return {'description': message, 'appended': info}
            setupCronJob(key_id=args.key_id, norad_id=args.norad_id)
        if action == 'append_keys':
            if args.key_id == None or args.n2yo_key == None or args.satnogs_key == None:
                abort(400, description="Must include all required parameters.")
            else:
                error, message = Sql().appendKeys(key_id=args.key_id, n2yo_key=args.n2yo_key, satnogs_key=args.satnogs_key)
                if error:
                    abort(500, description=message)
                if not error:
                    {'description': message}
        # webserver should authenticate and make sure user is an admin first
        if action == 'add_ground_station':
            if args.can_transmit == "True":
                can_transmit = True
            else:
                can_transmit = False
            if args.is_satnogs == "True":
                is_satnogs = True
            else:
                is_satnogs = False
            if args.name == None or args.lat == None or args.lng == None or args.alt == None or args.can_transmit == None or args.is_satnogs == None:
                abort(405, description="Missing ground station information.")
            else:
                error, message = Sql().addGroundstation(name=args.name, lat=args.lat, lng=args.lng, alt=args.alt, transmit=can_transmit, satnogs=is_satnogs)
                if error:
                    abort(500, description=message)
                if not error:
                    return {'description': message}
        
        else:
            abort(405, description="Nonexsistent action or incorrect use case.")


    def delete(self, action):
        print("hi")
        print(action)
        if action != 'delete_satellite':
            abort(405, description='Nonexsistent action or incorrect use case.')
        args = parser.parse_args()
        error, message = Sql().deleteSatellite(norad_id=args.norad_id)
        if not error:
            return {'description': message}
        else:
            abort(401, description=message)

