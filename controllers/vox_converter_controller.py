import io
import tempfile

from flask import make_response, send_file

from services.block import Block
from services.location import Location
from services.palette import Palette
from services.vox_parser import VoxParser
from services.voxel_converter import VoxConverter


class VoxConverterController:
    def __init__(self, vox_file, palette_file = None, block_id= None, location= None) -> None:
        
        self.voxel = VoxParser(vox_file)
        if not self.voxel.is_valid:
            self.response = make_response("O tipo de arquivo vox não é suportado",400)
            return
        
        self.build_options = {"palette":None,"block":None ,"location": None}

        if palette_file: 
            self.build_options["palette"] = Palette(palette_file)
            if not self.build_options["palette"].is_valide:
                self.response = make_response("A paleta não é valido",400)
                return
        else:
            self.build_options["palette"] = Palette()
        
        if block_id:
            self.build_options["block"] = Block(block_id)
            if not self.build_options["block"].is_valid:
                self.response = make_response("A Block id não é valido",400)
                return
            
        if location:
            self.build_options["location"] = Location(location)
            if not self.build_options["location"].is_valid:
                self.response = make_response("O Local de construção não é valido",400)
                return
 
        vox_converter = VoxConverter(self.voxel, self.build_options)
        file_name = f"{vox_file.filename.split('.')[0]}.lua"
        
        result = vox_converter.generate_lua_script()

        buffer = io.BytesIO()
        buffer.write( result.encode('utf-8'))
        buffer.seek(0)  

        self.response = send_file(buffer, mimetype='text/plain', as_attachment=True, download_name=file_name)
       


    



