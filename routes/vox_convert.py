from flask import jsonify
from flask_restful import Resource, reqparse, request

request_put_args = reqparse.RequestParser()
# request_put_args.add_argument("id_sender", type=int, help="id_sender is required.")

class VoxConverter(Resource):
    def get(self):
        return jsonify("Hello")

    def post(self):
    
        vox_file = request.files.get("vox")
        print(vox_file.filename)

        palette_file = request.files.get("palette")
        print(palette_file.stream)

        return "On Progress"
       
        