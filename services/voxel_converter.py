from src.utils import block_color_data, color_distance, generate_lua_base_code


class VoxConverter():
    def __init__(self,vox_parser, build_options) -> str:
        self.build_options = build_options
        self.vox_parser = vox_parser

    def generate_lua_script(self) -> str:
        positions = self.generate_position_table()
        size = self.generate_size_table()
        lua_base_code = generate_lua_base_code(self.build_options)

        if self.build_options["block"]:
            return f"{positions}\n{size}\n{lua_base_code}"
        
        blocks = self.generate_block_table() 
        return f"{positions}\n{blocks}\n{size}\n{lua_base_code}"

    def generate_position_table(self) -> str:
        position_table = 'blocks_positions = {'
        
        for voxel in self.vox_parser.voxels:
            position_line = '{'+f'{voxel.x},{voxel.y},{voxel.z},{voxel.c}'+'}'
            position_table = position_table + position_line + ','

        return position_table.strip(',') + '}'
    
    def get_block_list(self) -> list[tuple]:
        
        block_list = []
        processed_colors = {}

        for color in self.build_options["palette"].colors:
            if str(color) not in processed_colors:
                block = block_color_data[0]
                mim_delta_E = color_distance((color.r,color.g,color.b),(block.r,block.g,block.b))

                for block in block_color_data:
                    delta_E = color_distance((color.r,color.g,color.b),(block.r,block.g,block.b)) 

                    if mim_delta_E >= delta_E:
                        mim_delta_E = delta_E
                        mim_delta_E_block = block

                block_list.append(mim_delta_E_block)

                processed_colors[str(color)] = mim_delta_E_block    
                continue     
            block_list.append(processed_colors[str(color)])

        return block_list

    def generate_block_table(self) -> str:
        block_list = self.get_block_list()
        blocks_table = 'blocks_palette = {'

        for block in block_list:
            block_line = '{'+f'{block.block_id},{block.color_data}'+'}'
            blocks_table = blocks_table + block_line + ','

        return blocks_table.strip(',') + '}'
    
    def generate_size_table(self) -> str:
        size =  self.vox_parser.size
        return 'size = {' + f'x= {size.x},y= {size.y},z ={size.z}' + '}'
    
    def read_text(self, path: str) -> str:
        with open(path,"r") as file:
            return "".join(file.readlines())    
        
