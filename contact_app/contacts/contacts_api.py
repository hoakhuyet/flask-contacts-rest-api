from flask import Blueprint, json, jsonify, request
from flask_restful import Resource, Api, reqparse
from .contacts_controller import ContactController
from .contacts_model import Contacts

bp_contact = Blueprint('contacts', __name__)
api_contact = Api(bp_contact)


PARSER = reqparse.RequestParser()
PARSER.add_argument('data')


class ContactsAPI(Resource):
    def get(self, contact_id):
        controller = ContactController()
        contact = controller.get_contact_by_contact_id(contact_id)
        return jsonify(contact.get_dict_obj())

    def put(self, contact_id):
        args = PARSER.parse_args()
        data = args['data']
        dict_data = json.loads(data)
        controller = ContactController()
        contact = controller.get_contact_by_contact_id(contact_id)
        contact.set_data_form_dict(dict_data)
        # contact = Contacts(0, dict_data['name'], dict_data['phone'], dict_data['address'])
        controller = ContactController()
        if controller.update_contact(contact):
            return "update susscess", 200
        else:
            return "update fail", 503

    def delete(self, contact_id):
        controller = ContactController()
        if controller.delete_contact(contact_id):
            return "delete susscess", 200
        else:
            return "delete fail", 200


class ContactsListAPI(Resource):
    def post(self):
        args = PARSER.parse_args()
        data = args['data']
        dict_data = json.loads(data)
        contact = Contacts(0, dict_data['name'], dict_data['phone'], dict_data['address'])
        controller = ContactController()
        if controller.add_contact(contact):
            return "add susscess", 200
        else:
            return "add fail", 503

    def get(self):
        try:
            controller = ContactController()
            contacts = controller.get_all_contact()
            lst = []
            for contact in contacts:
                lst.append(contact.get_dict_obj())
            return jsonify(items=lst, count_all=len(lst))
        except Exception as ex:
            return ex.__str__(), 500


api_contact.add_resource(ContactsAPI, '/contacts/<contact_id>')
api_contact.add_resource(ContactsListAPI, '/contacts/')

