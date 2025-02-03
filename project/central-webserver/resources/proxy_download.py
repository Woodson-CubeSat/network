from flask import Response, request
from flask_restful import Resource, abort
from common.constants import GENERAL_API_URL
import requests

from flask import send_from_directory, abort, after_this_request
from flask_restful import Resource
import os

class ProxyDownload(Resource):
    def get(self, filename):
        try:
            # Forward the request to the database API
            db_response = requests.get(f'{GENERAL_API_URL}/download_telemetry/{filename}', stream=True)
            
            if db_response.status_code == 200:
                # Stream the file back to the client
                return Response(
                    db_response.iter_content(chunk_size=8192),
                    content_type=db_response.headers.get('Content-Type', 'application/octet-stream'),
                    headers={
                        'Content-Disposition': db_response.headers.get(
                            'Content-Disposition',
                            f'attachment; filename="{filename}"'
                        )
                    },
                    status=db_response.status_code
                )
            else:
                # Safely handle non-200 responses
                try:
                    # Attempt to parse error response as JSON
                    error_message = db_response.json().get("message", "An error occurred.")
                except ValueError:
                    # Default to raw text if JSON decoding fails
                    error_message = db_response.text or "An error occurred."
                
                # Return the error response to the client
                return {"error": error_message}, db_response.status_code

        except requests.exceptions.RequestException as e:
            # Handle request exceptions (e.g., connection errors, timeouts)
            return {"error": f"Proxy error: {str(e)}"}, 500