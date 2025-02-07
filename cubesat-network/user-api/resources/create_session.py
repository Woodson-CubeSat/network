from flask_restful import reqparse, Resource, abort
from flask_jwt_extended import create_access_token
from datetime import timedelta
from utils.db_token import CacheDBKey
from common.handler import SecureSql
from common.constants import TTL

# Parser for incoming requests
parser = reqparse.RequestParser()
parser.add_argument('UserID', type=str, location='headers')
parser.add_argument('Password', type=str, location='headers')
parser.add_argument('DBKey', type=str, location='headers')

class CreateSession(Resource):

    def get(self):
        args = parser.parse_args()
        user_id = args.UserID
        password = args.Password
        db_key = args.DBKey
        print(user_id, db_key, password)

        # Authenticate user with SecureSql
        secure_sql = SecureSql()
        print('got here')
        error, is_admin, message = secure_sql.authenticate(id=user_id, passwd=password, key_db_pass=db_key)
        print("you did it!")
        if error:
            abort(401, description=message)  # Authentication failed
        print("is_admin", is_admin, "error", error)
        # Cache the key_db_token
        cache = CacheDBKey()
        print(f"\n\n\nDB Key: {db_key}\n\n\n")
        cache.storeKey(user_id, db_key)
        print(f"\n\n\nRetrieved Key: {cache.getKey(user_id)}\n\n")

        # Generate a JWT
        access_token = create_access_token(
            identity=user_id,
            additional_claims={"is_admin": bool(is_admin)},
            expires_delta=timedelta(seconds=TTL)
        )

        return {"description": f"Successfully authenticated user {user_id}.", "token": access_token}, 200