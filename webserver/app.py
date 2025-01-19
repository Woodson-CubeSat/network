from flask import Flask
from flask_restful import Api
from resources.manage_api import ManageAPI
from webserver.resources.proxy_download import DownloadTelemetry

# start flask app
app = Flask(__name__)
api = Api(app)

# routing
api.add_resource(ManageAPI, '/api/<string:action>')
api.add_resource(DownloadTelemetry, '/download_telemetry/<string:filename>')


if __name__ == '__main__':
    app.run(debug=True)