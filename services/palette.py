from collections import namedtuple

from PIL import Image

Color = namedtuple("Color", "r g b a")

class Palette():
    def __init__(self, palette_file=None) -> None:
        if palette_file:
            self.palette_file = palette_file
            self.is_valide = self.load_palette(self.palette_file.stream)
            self.colors = self.get_colors()
            return
        
        self.is_valide = True
        self.colors = [Color(r=1, g=0, b=0, a=255), Color(r=21, g=13, b=13, a=255), Color(r=38, g=3, b=3, a=255), Color(r=22, g=37, b=41, a=255), Color(r=53, g=57, b=55, a=255), Color(r=60, g=47, b=51, a=255), Color(r=2, g=88, b=5, a=255), Color(r=0, g=73, b=57, a=255), Color(r=2, g=102, b=3, a=255), Color(r=1, g=102, b=63, a=255), Color(r=0, g=102, b=88, a=255), Color(r=0, g=100, b=103, a=255), Color(r=1, g=120, b=103, a=255), Color(r=119, g=70, b=58, a=255), Color(r=105, g=89, b=100, a=255), Color(r=101, g=100, b=103, a=255), Color(r=118, g=118, b=120, a=255), Color(r=7, g=21, b=135, a=255), Color(r=40, g=10, b=150, a=255), Color(r=37, g=26, b=159, a=255), Color(r=12, g=54, b=171, a=255), Color(r=40, g=34, b=167, a=255), Color(r=86, g=6, b=149, a=255), Color(r=104, g=23, b=151, a=255), Color(r=122, g=0, b=255, a=255), Color(r=48, g=74, b=166, a=255), Color(r=0, g=89, b=154, a=255), Color(r=0, g=67, b=169, a=255), Color(r=6, g=70, b=181, a=255), Color(r=0, g=84, b=170, a=255), Color(r=2, g=84, b=184, a=255), Color(r=0, g=121, b=163, a=255), Color(r=21, g=78, b=232, a=255), Color(r=4, g=88, b=254, a=255), Color(r=39, g=75, b=198, a=255), Color(r=54, g=68, b=196, a=255), Color(r=4, g=101, b=201, a=255), Color(r=9, g=100, b=214, a=255), Color(r=2, g=121, b=201, a=255), Color(r=1, g=119, b=215, a=255), Color(r=2, g=100, b=254, a=255), Color(r=23, g=103, b=254, a=255), Color(r=1, g=119, b=233, a=255), Color(r=1, g=120, b=252, a=255), Color(r=54, g=114, b=252, a=255), Color(r=250, g=0, b=3, a=255), Color(r=232, g=40, b=3, a=255), Color(r=247, g=38, b=4, a=255), Color(r=234, g=53, b=3, a=255), Color(r=251, g=56, b=2, a=255), Color(r=254, g=39, b=37, a=255), Color(r=251, g=52, b=40, a=255), Color(r=254, g=55, b=53, a=255), Color(r=254, g=4, b=71, a=255), Color(r=250, g=5, b=88, a=255), Color(r=250, g=20, b=88, a=255), Color(r=250, g=5, b=101, a=255), Color(r=250, g=25, b=89, a=255), Color(r=253, g=56, b=120, a=255), Color(r=146, g=118, b=0, a=255), Color(r=133, g=83, b=72, a=255), Color(r=151, g=112, b=112, a=255), Color(r=229, g=72, b=0, a=255), Color(r=252, g=72, b=2, a=255), Color(r=252, g=85, b=4, a=255), Color(r=251, g=106, b=2, a=255), Color(r=253, g=117, b=2, a=255), Color(r=244, g=105, b=56, a=255), Color(r=251, g=116, b=48, a=255), Color(r=198, g=88, b=71, a=255), Color(r=253, g=74, b=87, a=255), Color(r=251, g=87, b=72, a=255), Color(r=250, g=118, b=121, a=255), Color(r=135, g=9, b=167, a=255), Color(r=152, g=23, b=180, a=255), Color(r=181, g=24, b=180, a=255), Color(r=253, g=58, b=135, a=255), Color(r=229, g=25, b=211, a=255), Color(r=253, g=0, b=252, a=255), Color(r=138, g=86, b=214, a=255), Color(r=148, g=72, b=253, a=255), Color(r=196, g=114, b=195, a=255), Color(r=229, g=89, b=179, a=255), Color(r=230, g=103, b=216, a=255), Color(r=0, g=148, b=39, a=255), Color(r=2, g=167, b=54, a=255), Color(r=2, g=145, b=95, a=255), Color(r=0, g=136, b=118, a=255), Color(r=1, g=152, b=118, a=255), Color(r=1, g=167, b=69, a=255), Color(r=2, g=216, b=37, a=255), Color(r=0, g=247, b=102, a=255), Color(r=0, g=138, b=134, a=255), Color(r=0, g=135, b=151, a=255), Color(r=1, g=152, b=142, a=255), Color(r=0, g=133, b=167, a=255), Color(r=0, g=163, b=170, a=255), Color(r=0, g=167, b=172, a=255), Color(r=4, g=179, b=166, a=255), Color(r=0, g=186, b=183, a=255), Color(r=1, g=137, b=215, a=255), Color(r=1, g=150, b=200, a=255), Color(r=3, g=138, b=232, a=255), Color(r=5, g=138, b=252, a=255), Color(r=5, g=149, b=234, a=255), Color(r=2, g=152, b=252, a=255), Color(r=23, g=151, b=243, a=255), Color(r=0, g=181, b=213, a=255), Color(r=3, g=169, b=252, a=255), Color(r=3, g=183, b=233, a=255), Color(r=1, g=183, b=253, a=255), Color(r=67, g=184, b=254, a=255), Color(r=49, g=192, b=204, a=255), Color(r=1, g=220, b=177, a=255), Color(r=0, g=249, b=184, a=255), Color(r=5, g=198, b=201, a=255), Color(r=1, g=199, b=215, a=255), Color(r=0, g=199, b=231, a=255), Color(r=1, g=199, b=251, a=255), Color(r=2, g=214, b=233, a=255), Color(r=0, g=215, b=248, a=255), Color(r=16, g=241, b=212, a=255), Color(r=0, g=252, b=217, a=255), Color(r=3, g=231, b=254, a=255), Color(r=26, g=233, b=251, a=255), Color(r=1, g=252, b=230, a=255), Color(r=1, g=251, b=251, a=255), Color(r=20, g=246, b=250, a=255), Color(r=38, g=231, b=251, a=255), Color(r=55, g=230, b=253, a=255), Color(r=72, g=211, b=208, a=255), Color(r=70, g=218, b=252, a=255), Color(r=106, g=215, b=251, a=255), Color(r=119, g=215, b=253, a=255), Color(r=167, g=168, b=0, a=255), Color(r=183, g=180, b=1, a=255), Color(r=232, g=134, b=3, a=255), Color(r=253, g=135, b=1, a=255), Color(r=248, g=135, b=20, a=255), Color(r=253, g=151, b=1, a=255), Color(r=252, g=166, b=4, a=255), Color(r=233, g=183, b=1, a=255), Color(r=253, g=184, b=1, a=255), Color(r=253, g=179, b=37, a=255), Color(r=253, g=181, b=38, a=255), Color(r=251, g=183, b=54, a=255), Color(r=251, g=138, b=89, a=255), Color(r=247, g=165, b=94, a=255), Color(r=217, g=194, b=70, a=255), Color(r=165, g=249, b=4, a=255), Color(r=200, g=214, b=4, a=255), Color(r=253, g=201, b=2, a=255), Color(r=253, g=212, b=2, a=255), Color(r=252, g=216, b=23, a=255), Color(r=236, g=215, b=32, a=255), Color(r=217, g=231, b=23, a=255), Color(r=201, g=252, b=1, a=255), Color(r=216, g=229, b=39, a=255), Color(r=253, g=230, b=4, a=255), Color(r=252, g=232, b=23, a=255), Color(r=253, g=251, b=4, a=255), Color(r=252, g=250, b=22, a=255), Color(r=230, g=233, b=57, a=255), Color(r=251, g=230, b=38, a=255), Color(r=252, g=228, b=53, a=255), Color(r=252, g=252, b=38, a=255), Color(r=251, g=251, b=58, a=255), Color(r=253, g=217, b=94, a=255), Color(r=223, g=233, b=70, a=255), Color(r=252, g=232, b=67, a=255), Color(r=253, g=250, b=67, a=255), Color(r=244, g=238, b=120, a=255), Color(r=253, g=253, b=104, a=255), Color(r=253, g=250, b=119, a=255), Color(r=182, g=139, b=135, a=255), Color(r=167, g=151, b=151, a=255), Color(r=149, g=171, b=183, a=255), Color(r=167, g=169, b=168, a=255), Color(r=156, g=173, b=224, a=255), Color(r=215, g=155, b=175, a=255), Color(r=251, g=144, b=146, a=255), Color(r=253, g=147, b=172, a=255), Color(r=253, g=151, b=183, a=255), Color(r=206, g=183, b=175, a=255), Color(r=252, g=167, b=136, a=255), Color(r=252, g=175, b=146, a=255), Color(r=253, g=181, b=150, a=255), Color(r=252, g=163, b=166, a=255), Color(r=253, g=169, b=183, a=255), Color(r=250, g=184, b=164, a=255), Color(r=214, g=137, b=253, a=255), Color(r=253, g=154, b=199, a=255), Color(r=252, g=134, b=253, a=255), Color(r=244, g=153, b=230, a=255), Color(r=201, g=166, b=240, a=255), Color(r=207, g=188, b=187, a=255), Color(r=150, g=218, b=181, a=255), Color(r=169, g=229, b=135, a=255), Color(r=185, g=250, b=184, a=255), Color(r=155, g=249, b=253, a=255), Color(r=167, g=253, b=213, a=255), Color(r=183, g=248, b=216, a=255), Color(r=167, g=236, b=232, a=255), Color(r=168, g=230, b=251, a=255), Color(r=179, g=237, b=249, a=255), Color(r=164, g=244, b=251, a=255), Color(r=253, g=214, b=138, a=255), Color(r=254, g=217, b=155, a=255), Color(r=252, g=202, b=177, a=255), Color(r=253, g=217, b=165, a=255), Color(r=252, g=216, b=182, a=255), Color(r=201, g=254, b=150, a=255), Color(r=200, g=241, b=173, a=255), Color(r=254, g=234, b=134, a=255), Color(r=252, g=232, b=149, a=255), Color(r=235, g=251, b=134, a=255), Color(r=253, g=252, b=135, a=255), Color(r=253, g=251, b=152, a=255), Color(r=252, g=229, b=168, a=255), Color(r=249, g=239, b=181, a=255), Color(r=252, g=252, b=166, a=255), Color(r=251, g=247, b=186, a=255), Color(r=199, g=200, b=202, a=255), Color(r=217, g=214, b=218, a=255), Color(r=200, g=217, b=253, a=255), Color(r=214, g=213, b=252, a=255), Color(r=252, g=201, b=199, a=255), Color(r=248, g=203, b=216, a=255), Color(r=251, g=214, b=198, a=255), Color(r=252, g=214, b=214, a=255), Color(r=233, g=206, b=250, a=255), Color(r=253, g=199, b=228, a=255), Color(r=250, g=202, b=250, a=255), Color(r=231, g=210, b=253, a=255), Color(r=254, g=217, b=231, a=255), Color(r=250, g=218, b=251, a=255), Color(r=201, g=247, b=215, a=255), Color(r=213, g=246, b=208, a=255), Color(r=204, g=228, b=241, a=255), Color(r=200, g=250, b=252, a=255), Color(r=215, g=253, b=251, a=255), Color(r=248, g=232, b=203, a=255), Color(r=253, g=231, b=216, a=255), Color(r=231, g=251, b=202, a=255), Color(r=232, g=252, b=215, a=255), Color(r=254, g=252, b=200, a=255), Color(r=254, g=253, b=213, a=255), Color(r=231, g=232, b=232, a=255), Color(r=232, g=236, b=246, a=255), Color(r=250, g=234, b=233, a=255), Color(r=252, g=233, b=249, a=255), Color(r=233, g=254, b=232, a=255), Color(r=232, g=250, b=251, a=255), Color(r=254, g=253, b=232, a=255), Color(r=252, g=251, b=251, a=255), Color(r=0, g=0, b=0, a=0)]

    def load_palette(self, stream) -> bool:
        self.image = Image.open(stream)
        self.image.convert("RGBA")
        width, height = self.image.size
        return width == 256 and height == 1 

    def get_colors(self) ->list [Color]:
        pixels = list(self.image.getdata())
        return [Color(r, g, b, a) for (r, g, b, a) in pixels]
            
