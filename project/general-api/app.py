from flask import Flask
from flask_restful import Api
from resources.general import ManageDB
from resources.download_telemetry import DownloadTelemetry
from apscheduler.schedulers.background import BackgroundScheduler
import os
import time
from common.constants import script_dir, expiration_time

# start flask app
app = Flask(__name__)
api = Api(app)

# routing
api.add_resource(ManageDB, '/<string:action>')
api.add_resource(DownloadTelemetry, '/download_telemetry/<string:filename>')

# File cleanup task

scheduler = BackgroundScheduler()

def clean_old_files():
    current_time = time.time()
    for filename in os.listdir():
        file_path = os.path.join(f"{script_dir}/common/telemetry_cache", filename)
        if os.path.isfile(file_path):
            file_age = current_time - os.path.getmtime(file_path)
            if file_age > expiration_time:
                try:
                    os.remove(file_path)
                    print(f"Deleted old file: {filename}")
                except Exception as e:
                    print(f"Error deleting file {filename}: {e}")

# Schedule cleanup every hour
scheduler.add_job(clean_old_files, 'interval', hours=1)
scheduler.start()


if __name__ == '__main__':
    app.run(debug=True, port=8000)