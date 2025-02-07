from flask import Flask
from flask_restful import Api
from resources.manage_api import ManageData
from resources.manage_users import ManageUsers
from resources.proxy_download import ProxyDownload

# start flask app
app = Flask(__name__)
api = Api(app)

# routing
api.add_resource(ManageData, '/data/<string:action>')
api.add_resource(ManageUsers, '/users/<string:action>')
api.add_resource(ProxyDownload, '/download_telemetry/<string:filename>')


if __name__ == '__main__':
    app.run(debug=True)