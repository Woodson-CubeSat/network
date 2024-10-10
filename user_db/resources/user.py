from flask import Flask
from flask_restful import fields, marshal_with, reqparse, Resource
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


# options for data
parser.add_argument('email_login', type=bool, location='form')
parser.add_argument('is_admin', type=bool, location='form')
parser.add_argument('callsign', type=bool, location='form')
parser.add_argument('key_id', type=bool, location='form')


class user(Resource):

    #@marshal_with(user_info)
    def get(self):
        args = parser.parse_args()
        print(type(args.email_login))
        secureSql().getUserInfo(user_id=args.UserID, passwd_hash=args.Password, key_db_token=args.DBKey, email_login=args.email_login, is_admin=args.is_admin, callsign=args.callsign, key_id=args.key_id)
        

    def put(self):
        pass

    def delete(self):
        pass

