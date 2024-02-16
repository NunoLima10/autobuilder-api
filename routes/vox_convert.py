from flask import jsonify, make_response
from flask_restful import Resource, request
from controllers.vox_converter_controller import VoxConverterController



class VoxConverter(Resource):
    def get(self):
        return jsonify("Hello")

    def post(self):
        vox_file = request.files.get("vox")
        # print(vox_file.filename)
        palette_file = request.files.get("palette")
        # print(palette_file.stream)

        controller = VoxConverterController(vox_file, palette_file)

        return controller.response
       
        