from flask import Blueprint, json, jsonify, request
from flask_restful import Resource, Api, reqparse

bp_users = Blueprint('users', __name__)
api_users = Api(bp_users)

class Users(Resource):
    def get(self, requirements):
        return jsonify({
            "status_code": 200,
            "text": requirements
        })

    def put(self, user_name):
        pass


    def delete(self, user_name):
        pass

class UsersList(Resource):
    def post(self):
        pass
    
    def get(self, user_name):
       pass


api_users.add_resource(Users, '/users/<requirements>')
api_users.add_resource(UsersList, '/users/')
