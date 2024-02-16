from flask import send_file
from flask_restful import Resource

class Palette(Resource):
    def get(self):
        return send_file("static\palettes\Mini_World_color_palette.png")