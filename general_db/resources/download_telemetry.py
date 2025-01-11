from flask import send_from_directory
from flask_restful import Resource, abort
import os


from flask import send_from_directory, abort, after_this_request
from flask_restful import Resource
import os

class DownloadTelemetry(Resource):
    def get(self, filename):
        try:
            # Define the directory where the zip files are stored
            directory = 'telemetry_cache'

            # Check if the file exists in the directory
            file_path = os.path.join(directory, filename)
            if not os.path.isfile(file_path):
                # If the file doesn't exist, return a 404 error
                abort(404, message=f"File {filename} not found.")

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
            return send_from_directory(directory, filename, as_attachment=True)

        except Exception as e:
            # Return an error message if anything goes wrong
            abort(500, message=f"Error: {str(e)}")