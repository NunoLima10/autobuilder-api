import tempfile
from flask import send_file,make_response

from services.palette import Palette
from services.vox_parser import VoxParser
from services.voxel_converter import VoxConverter
class VoxConverterController:
    def __init__(self, vox_file, palette_file) -> None:

        self.palette = Palette(palette_file)
        print(self.palette.is_valide)
        if not self.palette.is_valide:
            self.response = make_response("A paleta enviada não é suportada",400)
            return
            
        self.voxel = VoxParser(vox_file)
        if  not self.voxel.is_valid:
            self.response = make_response("O tipo de arquivo vox não é suportado",400)
            return
            
        vox_converter = VoxConverter(self.palette,self.voxel)
        file_name = f"{vox_file.filename.split('.')[0]}.lua"
        
        result = vox_converter.generate_lua_script()

        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(result.encode("utf-8"))

        self.response = send_file(tmp_file.name, mimetype='text/plain', as_attachment=True, download_name=file_name)
       


    



