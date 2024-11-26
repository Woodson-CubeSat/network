from flask import Flask
from flask_restful import reqparse, Resource, abort
from common.handler import secureSql


parser = reqparse.RequestParser()
parser.add_argument('UserID', type=str, location='headers')
parser.add_argument('Password', type=str, location='headers')
parser.add_argument('DBKey', type=str, location='headers')


class authenticate(Resource):

    def get(self):
        args = parser.parse_args()
        error, error_message = secureSql().authenticate(id=args.UserID, passwd=args.Password, key_db_pass=args.DBKey)
        if not error_message:
            return {'message': 'Successfully authenticated user.'} # also returns code 200, or success
        else:
            abort(401, message=error_message) # code 401 means unauthorized