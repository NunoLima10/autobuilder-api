from PIL import Image

from collections import namedtuple
Color = namedtuple("Color", "r g b a")

class Palette():
    def __init__(self, palette_file) -> None:
        self.palette_file = palette_file
        self.is_valide = self.load_palette(self.palette_file.stream)
        

    def load_palette(self, stream) -> bool:
        self.image = Image.open(stream)
        self.image.convert("RGBA")
        width, height = self.image.size
        return width == 256 and height == 1 

    def get_colors(self) ->list [Color]:
        pixels = list(self.image.getdata())
        return [Color(r, g, b, a) for (r, g, b, a) in pixels]
            
