import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource

from routes.palette import Palette
from routes.vox_convert import VoxConverter

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)
load_dotenv()

port = os.getenv("PORT") or 5000
        
class MiniWorldAutoBuilder(Resource):
     def get(self):
        return  "Hello from MiniWorldAutoBuilder"
     
if __name__=="__main__":

    api.add_resource(MiniWorldAutoBuilder,"/")
    api.add_resource(VoxConverter,"/converter")
    api.add_resource(Palette, "/palette")
    app.run(host='0.0.0.0', port=5000,debug=True)
