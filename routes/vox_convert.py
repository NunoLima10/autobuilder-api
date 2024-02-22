from flask_restful import Resource, request
from controllers.vox_converter_controller import VoxConverterController


class VoxConverter(Resource):
    def post(self):
        vox_file = request.files.get("vox")
        palette_file = request.files.get("palette")
        build_location = None
        # build_location = [int(value) for value in request.form.getlist("location[]")[0].split(',')]
       
        
        build_location = request.form.getlist("location[]")
        block_id = request.form.get("block")
     
        controller = VoxConverterController(vox_file, palette_file, block_id, build_location)

        return controller.response
       
        