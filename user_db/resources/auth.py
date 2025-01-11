from flask_restful import reqparse, Resource, abort
from flask_jwt_extended import create_access_token
from utils.db_token import CacheDBKey
from common.handler import SecureSql
from datetime import timedelta
from common.constants import ttl

# Parser for incoming requests
parser = reqparse.RequestParser()
parser.add_argument('UserID', type=str, location='headers', required=True, help='UserID is required')
parser.add_argument('Password', type=str, location='headers', required=True, help='Password is required')
parser.add_argument('DBKey', type=str, location='headers', required=True, help='DBKey is required')

class Authenticate(Resource):

    def get(self):
        args = parser.parse_args()
        user_id = args.UserID
        password = args.Password
        db_key = args.DBKey
        print(user_id, db_key, password)

        # Authenticate user with SecureSql
        secure_sql = SecureSql()
        error, is_admin, message = secure_sql.authenticate(id=user_id, passwd=password, key_db_pass=db_key)
        if error:
            abort(401, message=message)  # Authentication failed

        # Cache the key_db_token
        cache = CacheDBKey()
        print(f"\n\n\nDB Key: {db_key}\n\n\n")
        cache.storeKey(user_id, db_key)
        print(f"\n\n\nRetrieved Key: {cache.getKey(user_id)}\n\n")

        # Generate a JWT
        access_token = create_access_token(
            identity=user_id,
            additional_claims={"is_admin": bool(is_admin)},
            expires_delta=timedelta(seconds=ttl)
        )

        return {"message": "Successfully authenticated user.", "token": access_token}, 200