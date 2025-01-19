from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from apscheduler.schedulers.background import BackgroundScheduler
from user_db.resources.create_session import CreateSession
from resources.user import ManageUsers
from common.constants import renew_secret_key
import os
import secrets

# Initialize Flask app
app = Flask(__name__)

# Set up JWT secret key
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', secrets.token_hex(32))

# Initialize JWTManager
jwt = JWTManager(app)

# Function to rotate secret key
def rotate_secret_key():
    app.config['JWT_SECRET_KEY'] = secrets.token_hex(32)
    print("JWT_SECRET_KEY rotated successfully")

# Schedule secret key rotation every hour
scheduler = BackgroundScheduler()
scheduler.add_job(rotate_secret_key, 'interval', hours=renew_secret_key)
scheduler.start()

# Initialize API
api = Api(app)

# Define routes
api.add_resource(CreateSession, '/create_session')
api.add_resource(ManageUsers, '/<action>')

if __name__ == '__main__':
    app.run(debug=True)