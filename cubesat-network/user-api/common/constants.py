import subprocess
import os

# Initialize script directory
script_dir = str(subprocess.check_output(["pwd"])).replace("b'", "").replace("n'", "")[:-1]
TTL = 3600 
DEFAULT_ADMIN_PASSWD =  "blablabla"
RENEW_SECRET_KEY = 12

# Parameters for Gunicorn
WORKERS = 2
THREADS = 4
BIND = '0.0.0.0:8000'
