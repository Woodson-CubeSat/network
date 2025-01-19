from flask import Flask
from flask_restful import fields, marshal_with, reqparse, Resource, abort
from common.handler import SecureSql
from utils.db_token import CacheDBKey
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt


# will end up basing webserver off of test.py requests and processing



parser = reqparse.RequestParser()

# Options for data (get)
parser.add_argument('get_email_login', type=bool, location='form')
parser.add_argument('is_admin', type=bool, location='form')
parser.add_argument('get_callsign', type=bool, location='form')
parser.add_argument('get_key_id', type=bool, location='form')
parser.add_argument('get_satnogs_cookies', type=bool, location='form')
parser.add_argument('get_creation_time', type=bool, location='form')


# Options for data (put)
parser.add_argument('email', type=str, location='form')
parser.add_argument('email_passwd', type=str, location='form')
parser.add_argument('satnogs_cookies', type=str, location='form')
parser.add_argument('callsign', type=str, location='form')
parser.add_argument('create_admin', type=bool, location='form')

# Options for data (delete)
parser.add_argument('user_id', type=str, location='form')

class ManageUsers(Resource):

    @jwt_required()
    def get(self, action):
        args = parser.parse_args()
        current_user = get_jwt_identity()  # Retrieves user_id
        claims = get_jwt()  # Retrieves all JWT claims
        is_admin = claims.get("is_admin", False)

        # Retrieve key_db_token from cache
        cache = CacheDBKey()
        key_db_token = cache.getKey(current_user)
        print(f"\n\n\nRetrieved Key: {cache.getKey(current_user)}\n\n")

        if not key_db_token:
            abort(401, message="Session expired. Please re-authenticate.")

        secure_sql = SecureSql()

        if action == 'get_info':
            error, message, info = secure_sql.getUserInfo(
                key_db_token=key_db_token,
                user_id=current_user,
                sudo=is_admin,
                email_login=args.get_email_login,
                is_admin=args.is_admin,
                callsign=args.get_callsign,
                key_id=args.get_key_id,
                satnogs_cookies=args.get_satnogs_cookies,
                creation_time=args.get_creation_time
            )
            if error:
                abort(400, message=message)
            return info, 200

        if action == "list_users":
            error, message, info = secure_sql.listUsers(sudo=is_admin, key_db_token=key_db_token)
            if error:
                abort(401, message=message)
            return info, 200
        
        if action == "jwt_auth" or action == "jwt":
            current_user = get_jwt_identity()  # Retrieves user_id
            claims = get_jwt()  # Retrieves all JWT claims
            is_admin = claims.get("is_admin", False)
            return {"user_id": current_user, "admin_status": is_admin}


        else:
            abort(405, message='Nonexistent action or incorrect use case.')


    @jwt_required()
    def put(self, action):
        args = parser.parse_args()
        current_user = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get("is_admin", False)

        # Retrieve key_db_token from cache
        cache = CacheDBKey()
        key_db_token = cache.getKey(current_user)
        print(f"\n\n\nRetrieved Key: {cache.getKey(current_user)}\n\n")
        print(key_db_token)
        if not key_db_token:
            abort(401, message="Session expired. Please re-authenticate.")

        secure_sql = SecureSql()

        if action == 'create_user':
            error, message, info = secure_sql.buildUserInfo(
                satnogs_cookies=args.satnogs_cookies,
                auth_user_id=current_user,
                sudo=is_admin,
                key_db_token=key_db_token,
                email=args.email,
                email_passwd=args.email_passwd,
                callsign=args.callsign,
                create_admin=args.create_admin
            )
            if error:
                abort(400, message=message)
            return info, 201

        elif action == 'update_info':
            error, message = secure_sql.updateUserInfo(
                user_id=current_user,
                sudo=is_admin,
                key_db_token=key_db_token,
                email=args.email,
                email_passwd=args.email_passwd,
                callsign=args.callsign
            )
            if error:
                abort(401, message=message)
            return {'message': message}, 200

        else:
            abort(405, message="Nonexistent action or incorrect use case.")

    @jwt_required()
    def delete(self, action):
        args = parser.parse_args()
        current_user = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get("is_admin", False)

        # Retrieve key_db_token from cache
        cache = CacheDBKey()
        key_db_token = cache.getKey(current_user)
        if not key_db_token:
            abort(401, message="Session expired. Please re-authenticate.")

        if action != 'delete_user':
            abort(405, message='Nonexistent action or incorrect use case.')

        secure_sql = SecureSql()
        error, message = secure_sql.deleteUser(
            sudo=is_admin,
            key_db_token=key_db_token,
            user_id=args.user_id
        )
        if error:
            abort(400, message=message)
        return {'message': 'Successfully deleted user.'}, 200

