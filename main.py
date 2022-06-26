from flask import Flask, request
from flask_cors  import cross_origin, CORS
from flask_restful import Resource, Api, abort, reqparse

app = Flask(_name_)
api = Api(app)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



class Employees(Resource):           
    def get(self):
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

api.add_resource(Employees, '/employees') # Route_1
    


if _name_ == '_main_':
    app.run(port=5050)