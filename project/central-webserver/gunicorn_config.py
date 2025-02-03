import os
from common.constants import WORKERS, THREADS, BIND



workers = int(os.environ.get('GUNICORN_PROCESSES', f'{WORKERS}'))

threads = int(os.environ.get('GUNICORN_THREADS', f'{THREADS}'))

# timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))

bind = os.environ.get('GUNICORN_BIND', f'{BIND}')



forwarded_allow_ips = '*'

# secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }