import os
# Transition to environment variables when deployed in docker containers
GENERAL_API_URL = "http://general-api:5500"
USER_API_URL = "http://user-api:8000"
DB_KEY = os.getenv("DB_KEY")

# Parameters for Gunicorn
WORKERS = 2
THREADS = 4
BIND = '0.0.0.0:3000'
