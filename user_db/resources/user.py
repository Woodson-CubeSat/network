from flask import Flask
from flask_restful import fields, marshal_with, reqparse, Resource, abort
from common.handler import secureSql


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

# authentication headers
parser.add_argument('UserID', type=str, location='headers', required=True)
parser.add_argument('Password', type=str, location='headers', required=True)
parser.add_argument('DBKey', type=str, location='headers', required=True)


# options for data (get)
parser.add_argument('get_email_login', type=bool, location='form')
parser.add_argument('is_admin', type=bool, location='form')
parser.add_argument('get_callsign', type=bool, location='form')
parser.add_argument('get_key_id', type=bool, location='form')
parser.add_argument('get_satnogs_cookies', type=bool, location='form')
parser.add_argument('get_creation_time', type=bool, location='form')


# options for data (put)
parser.add_argument('email', type=str, location='form')
parser.add_argument('email_passwd', type=str, location='form')
parser.add_argument('satnogs_cookies', type=str, location='form')
parser.add_argument('callsign', type=str, location='form')
parser.add_argument('create_admin', type=bool, location='form')

#options for data (delete)
parser.add_argument('user_id', type=str, location='form')

class manageUsers(Resource):

    #@marshal_with(get_struct)
    def get(self, action):
        args = parser.parse_args()
        if action == 'get_info':  
            
            print(type(args.get_satnogs_cookies))
            error, error_message, info = secureSql().getUserInfo(user_id=args.UserID, passwd=args.Password, key_db_token=args.DBKey, email_login=args.get_email_login, is_admin=args.is_admin, callsign=args.get_callsign, key_id=args.get_key_id, satnogs_cookies=args.get_satnogs_cookies, creation_time=args.get_creation_time)
            print(error)
            print(error_message)
            print(info)
            #if there is an error, the value for the error variable will be True
            if error:
                print("error")
                abort(401, message=error_message)
            if not error:
                return info
        if action == "list_users":
            error, error_message, info = secureSql().listUsers(user_id=args.UserID, passwd=args.Password, key_db_token=args.DBKey)
            if error:
                abort(401, message=error_message)
            if not error:
                return info
        else:
            abort(405, message='Nonexsistent action or incorrect use case.')


    def put(self, action):
        args = parser.parse_args()
        # for creating a user
        print("action "+action)
        if action == 'create_user' :
            error, error_message, info = secureSql().buildUserInfo(satnogs_cookies=args.satnogs_cookies, auth_user_id=args.UserID, auth_user_passwd=args.Password, key_db_token=args.DBKey, email=args.email, email_passwd=args.email_passwd, callsign=args.callsign, create_admin=args.create_admin)
            print(error)
            print(error_message)
            print(info)
            if error:
                print("error")
                abort(401, message=error_message)
            if not error:
                return info
        if action == 'update_info':
            error, message = secureSql().updateUserInfo(user_id=args.UserID, passwd=args.Password, key_db_token=args.DBKey, email=args.email, email_passwd=args.email_passwd, callsign=args.callsign)
            if error:
                abort(401, message=message)
            if not error:
                return {'message': message}
        else:
            abort(405, message="Nonexsistent action or incorrect use case.")


    def delete(self, action):
        print("hi")
        print(action)
        if action != 'delete_user':
            abort(405, message='Nonexsistent action or incorrect use case.')
        args = parser.parse_args()
        error, error_message = secureSql().deleteUser(auth_user_id=args.UserID, auth_user_passwd=args.Password, key_db_token=args.DBKey, user_id=args.user_id)
        if not error:
            return {'message': 'Successfully deleted user.'}
        else:
            abort(401, message=error_message)

