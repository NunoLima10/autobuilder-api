from flask_restful import Resource, request

from controllers.vox_converter_controller import VoxConverterController


class VoxConverter(Resource):
    def post(self):
        vox_file = request.files.get("vox")
        palette_file = request.files.get("palette")
     
        controller = VoxConverterController(vox_file, palette_file)

        return controller.response
       
        