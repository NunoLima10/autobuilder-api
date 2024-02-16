from flask import jsonify
from flask_restful import Resource, reqparse

request_put_args = reqparse.RequestParser()
# request_put_args.add_argument("id_sender", type=int, help="id_sender is required.")

class VoxConverter(Resource):
    def get(self):
        pass

    def post(self):
        pass