from flask import Flask
from flask_restful import Api,Resource
from flask_cors import CORS

from routes.vox_convert import VoxConverter
from routes.palette import Palette

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)
        

if __name__=="__main__":
    api.add_resource(VoxConverter,"/converter")
    api.add_resource(Palette, "/palette")
    app.run(host='0.0.0.0', port=5000,debug=True)
