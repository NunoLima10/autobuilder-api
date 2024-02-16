from flask import Flask
from flask_restful import Api,Resource

from routes.vox_convert import VoxConverter
from routes.palette import Palette

app = Flask(__name__)
api = Api(app)
        

if __name__=="__main__":
    api.add_resource(VoxConverter,"/converter")
    api.add_resource(Palette, "/palette")
    app.run(host='0.0.0.0', port=3000,debug=True)
