from flask import send_from_directory, abort, after_this_request
from flask_restful import Resource
import os
from common.constants import script_dir

class DownloadTelemetry(Resource):
    def get(self, filename):
        # try:
            # Define the directory where the zip files are stored
            directory = f"{script_dir}/common/telemetry_cache/"

            # Check if the file exists in the directory
            file_path = f"{script_dir}/common/telemetry_cache/{filename}"
            print(f"Expected file path: {file_path}")
            print(f"File exists: {os.path.isfile(file_path)}")
            if not os.path.isfile(file_path):
                # If the file doesn't exist, return a 404 error
                abort(404, description=f"File {filename} not found.")

            # Ensure the file is deleted after the response is sent
            @after_this_request
            def cleanup(response):
                try:
                    os.remove(file_path)
                    print(f"File {filename} deleted successfully.")
                except Exception as e:
                    print(f"Error deleting file {filename}: {str(e)}")
                return response

            # Send the file as an attachment for download
            print(directory)
            print(filename)
            return send_from_directory(directory, filename, as_attachment=True)

        # except Exception as e:
        #     # Return an error message if anything goes wrong
        #     abort(500, description=f"Error: {str(e)}")