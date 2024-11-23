from flask import Flask
from flask_restful import fields, marshal_with, reqparse, Resource, abort
from common.handler import secureSql
import base64
import pickle

# notes from 11/23/2024
# change (rewrite) getUserInfo and buildUserInfo (along with API side methods) to use get_struct and marshal_with
# add option to retrive creation time in getUserInfo
# finish testing delete user
# add new file for updating user data (like cookies)
# will end up basing webserver off of test.py requests and processing


get_struct = {'key_id': fields.String,
            'is_admin': fields.Integer,
            'callsign': fields.String,
            'email_info': fields.Nested({
                'email': fields.String,
                'email_passwd': fields.String
                })
            }

put_struct = {}

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
parser.add_argument('email', type=str, location='form')
parser.add_argument('email_passwd', type=str, location='form')
parser.add_argument('satnogs_cookies', type=str, location='form')
parser.add_argument('callsign', type=str, location='form')
parser.add_argument('create_admin', type=bool, location='form')



class user(Resource):

    def get(self):
        args = parser.parse_args()
        print(type(args.get_email_login))
        error, error_message, info = secureSql().getUserInfo(user_id=args.UserID, passwd_hash=args.Password, key_db_token=args.DBKey, email_login=args.get_email_login, is_admin=args.is_admin, callsign=args.get_callsign, key_id=args.get_key_id)
        print(error)
        print(error_message)
        print(info)
        #if there is an error, the value for the error variable will be True
        if error:
            print("error")
            abort(401, message=error_message)
        if not error:
            return info


    def put(self):
        args = parser.parse_args()
        # transmitted as cookie file turned into base64 turned into str (from bytestring)
        str_satnogs_cookie = args.satnogs_cookies
        # turn str object into base64 bytestring
        bytestring_satnogs_cookie = str_satnogs_cookie.encode('utf-8')
        # decode base64 into binary object
        satnogs_cookies = base64.decodebytes(bytestring_satnogs_cookie)
        print(satnogs_cookies)
        # testing
        cookies = pickle.loads(satnogs_cookies)
        print("loaded cookies")
        print(cookies)
        for cookie in cookies:
            print(cookie)
        error, error_message, info = secureSql().buildUserInfo(satnogs_cookies=satnogs_cookies, auth_user_id=args.UserID, auth_user_passwd=args.Password, key_db_token=args.DBKey, email=args.email, email_passwd=args.email_passwd, callsign=args.callsign, create_admin=args.create_admin)
        print(error)
        print(error_message)
        print(info)
        if error:
            print("error")
            abort(401, message=error_message)
        if not error:
            return info


    def delete(self):
        pass

