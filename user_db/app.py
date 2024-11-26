from flask import Flask
from flask_restful import Api
from resources.auth import authenticate
from resources.user import manageUsers

# start flask app
app = Flask(__name__)
api = Api(app)

# routing
api.add_resource(authenticate, '/auth')
api.add_resource(manageUsers, '/manage_users/<action>')

if __name__ == '__main__':
    app.run(debug=True)