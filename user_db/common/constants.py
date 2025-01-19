import subprocess

# Initialize script directory
script_dir = str(subprocess.check_output(["pwd"])).replace("b'", "").replace("n'", "")[:-1]
ttl = 3600  # Global TTL for JWT tokens and storing the key_db_token (seconds)
renew_secret_key = 12 # Controls secret key renewal (hours)
