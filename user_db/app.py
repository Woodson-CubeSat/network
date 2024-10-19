from flask import Flask
from flask_restful import Api
from resources.auth import authenticate
from resources.user import user

# start flask app
app = Flask(__name__)
api = Api(app)

# routing
api.add_resource(authenticate, '/auth')
api.add_resource(user, '/user_actions')

if __name__ == '__main__':
    app.run(debug=True)