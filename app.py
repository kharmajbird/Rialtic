#
# http://localhost/input?DOB=082471&first=James&last=Lewis
#

from flask import Flask
from flask import request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

class Input(Resource):
    def get(self):

        DOB = request.args.get('DOB')
        first = request.args.get('first')
        last = request.args.get('last')

        data = DOB + first + last
        data = hash(data)

        return {'data': data}, 200


api.add_resource(Input, '/input')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
