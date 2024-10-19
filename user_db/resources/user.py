from flask import Flask
from flask_restful import fields, reqparse, Resource, abort
from common.handler import secureSql


user_info = {'key_id': fields.String,
            'is_admin': fields.Integer,
            'callsign': fields.String,
            'email_info': fields.Nested({
                'email': fields.String,
                'email_passwd': fields.String
                })
            }

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


# options for data (put)

        # auth_user_id: str,
        # auth_user_passwd: str,
        # key_db_token: str,
        # email: str,
        # email_passwd: str,
        # key_id: str,
        # satnogs_cookie, # this will be a file in the form of hex or binary
        # n2yo_key: str,
        # callsign: str = None,
        # create_admin: bool = False

parser.add_argument('email', type=bool, location='form')
parser.add_argument('email_passwd', type=bool, location='form')
parser.add_argument('email', type=bool, location='form')



#options for data

class user(Resource):

    def get(self):
        args = parser.parse_args()
        print(type(args.email_login))
        error, error_message, info =secureSql().getUserInfo(user_id=args.UserID, passwd_hash=args.Password, key_db_token=args.DBKey, email_login=args.get_email_login, is_admin=args.is_admin, callsign=args.get_callsign, key_id=args.get_key_id)
        print(error)
        print(error_message)
        print(info)
        #if there is an error, the value for the error variable will be True
        if not error:
            print("error")
            abort(401, message=error_message)
        if error:
            return info


    def put(self):
        pass

    def delete(self):
        pass

