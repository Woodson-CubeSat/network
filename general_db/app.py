from flask import Flask
from flask_restful import Api
from resources.general import ManageDB
from resources.download_telemetry import DownloadTelemetry

# start flask app
app = Flask(__name__)
api = Api(app)

# routing
api.add_resource(ManageDB, '/<string:action>')
api.add_resource(DownloadTelemetry, '/download_telemetry/<string:filename>')


if __name__ == '__main__':
    app.run(debug=True)