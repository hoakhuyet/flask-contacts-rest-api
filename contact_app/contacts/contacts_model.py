from dbconnect import db


class Contacts(db.Model):
    __tablename__ = "Contacts"
    contact_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500))
    phone = db.Column(db.String(500))
    address = db.Column(db.String(500))

    def __init__(self, contact_id, name, phone, address):
        if contact_id != 0:
            self.contact_id = contact_id
        self.name = name
        self.phone = phone
        self.address = address

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.contact_id, self.name, self.phone, self.address)

    def get_dict_obj(self):
        return {
            "contact_id": str(self.contact_id),
            "name": self.name,
            "phone": self.phone,
            "address": self.address
        }

    def set_data_form_dict(self, dict_data):
        if "name" in dict_data:
            self.name = dict_data["name"]
        if "phone" in dict_data:
            self.phone = dict_data["phone"]
        if "address" in dict_data:
            self.address = dict_data["address"]
