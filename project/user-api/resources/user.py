from flask import Flask
from flask_restful import fields, marshal_with, reqparse, Resource, abort
from common.handler import SecureSql
from utils.db_token import CacheDBKey
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt


# will end up basing webserver off of test.py requests and processing



parser = reqparse.RequestParser()

# Options for data (get)
parser.add_argument('get_email_login', location='form')
parser.add_argument('is_admin', location='form')
parser.add_argument('get_callsign', location='form')
parser.add_argument('get_key_id', location='form')
parser.add_argument('get_satnogs_cookies', location='form')
parser.add_argument('get_creation_time', location='form')


# Options for data (put)
parser.add_argument('username', type=str, location='form')
parser.add_argument('passwd', type=str, location='form')
parser.add_argument('email', type=str, location='form')
parser.add_argument('email_passwd', type=str, location='form')
parser.add_argument('satnogs_cookies', type=str, location='form')
parser.add_argument('callsign', type=str, location='form')
parser.add_argument('create_admin', location='form', default=False)

# Options for data (delete)
parser.add_argument('user_id', type=str, location='form')

class ManageUsers(Resource):

    @jwt_required()
    def get(self, action):
        args = parser.parse_args()
        current_user = get_jwt_identity()  # Retrieves user_id
        claims = get_jwt()  # Retrieves all JWT claims
        jwt_admin = claims.get("is_admin", False)

        # Retrieve key_db_token from cache
        cache = CacheDBKey()
        key_db_token = cache.getKey(current_user)
        print(f"\n\n\nRetrieved Key: {cache.getKey(current_user)}\n\n")

        if not key_db_token:
            abort(401, description="Session expired. Please re-authenticate.")

        secure_sql = SecureSql()

        if action == 'get_info':
            # Fix for flask not supporting bools
            # Define a list of boolean-like fields
            boolean_fields = ['get_email_login', 'is_admin', 'get_callsign', 'get_key_id', 'get_satnogs_cookies', 'get_creation_time']

            dynamic_variables = {}
            # Dynamically create standalone variables
            for field in boolean_fields:
                print(field)
                value = args.get(field)  # Get the value of the argument
                print('value', value)
                # Convert "True" or "False" strings to actual booleans or None
                converted_value = value == "True" if value is not None else False
                dynamic_variables[field] = converted_value

            error, message, info = secure_sql.getUserInfo(
                key_db_token=key_db_token,
                user_id=current_user,
                sudo=jwt_admin,
                email_login=dynamic_variables["get_email_login"],
                is_admin=dynamic_variables["is_admin"],
                callsign=dynamic_variables["get_callsign"],
                key_id=dynamic_variables["get_key_id"],
                satnogs_cookies=dynamic_variables["get_satnogs_cookies"],
                creation_time=dynamic_variables["get_creation_time"]
            )
            print(info)
            if error:
                abort(400, description=message)
            return info, 200

        if action == "list_users":
            print('admin_check', jwt_admin)
            error, message, info = secure_sql.listUsers(sudo=jwt_admin, key_db_token=key_db_token)
            if error:
                abort(401, description=message)
            return info, 200
        
        if action == "jwt_auth" or action == "jwt":
            current_user = get_jwt_identity()  # Retrieves user_id
            claims = get_jwt()  # Retrieves all JWT claims
            is_admin = claims.get("is_admin", False)
            return {"user_id": current_user, "admin_status": is_admin}


        else:
            abort(405, description='Nonexistent action or incorrect use case.')


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
            abort(401, description="Session expired. Please re-authenticate.")

        secure_sql = SecureSql()

        if action == 'create_user':
            print('is_admin', args.create_admin, 'type', type(args.create_admin))
            if args.create_admin == "True":
                create_admin = True
            else:
                create_admin = False
            error, message, info = secure_sql.buildUserInfo(
                username=args.username,
                passwd=args.passwd,
                satnogs_cookies=args.satnogs_cookies,
                sudo=is_admin,
                key_db_token=key_db_token,
                email=args.email,
                email_passwd=args.email_passwd,
                callsign=args.callsign,
                create_admin=create_admin
            )
            if error:
                abort(400, description=message)
            return info, 201

        elif action == 'update_info':
            error, message = secure_sql.updateUserInfo(
                user_id=current_user,
                key_db_token=key_db_token,
                email=args.email,
                email_passwd=args.email_passwd,
                satnogs_cookies=args.satnogs_cookies,
                callsign=args.callsign,
                passwd = args.passwd
            )
            if error:
                abort(401, description=message)
            return {'description': message}, 200

        else:
            abort(405, description="Nonexistent action or incorrect use case.")

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
            abort(401, description="Session expired. Please re-authenticate.")

        if action != 'delete_user':
            abort(405, description='Nonexistent action or incorrect use case.')

        secure_sql = SecureSql()
        error, message = secure_sql.deleteUser(
            sudo=is_admin,
            key_db_token=key_db_token,
            user_id=args.user_id
        )
        if error:
            abort(400, description=message)
        return {'description': 'Successfully deleted user.'}, 200

