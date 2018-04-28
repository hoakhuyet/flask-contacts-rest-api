from flask import abort
from flask_sqlalchemy import orm
from .contacts_model import Contacts
from dbconnect import db
# from contact_app.dbconnect import db


class ContactController:
    def __init__(self):
        pass

    def get_contact_by_contact_id(self, contact_id):
        try:
            base_query_transaction = db.session().query(Contacts).filter_by(contact_id=contact_id)
            if len(base_query_transaction.all()) > 0:
                return base_query_transaction[0]
            else:
                raise abort(404, "contact_app not found")
                # return None
        except Exception as ex:
            abort(500, "internal server error")
            return None

    def get_all_contact(self, limit=0):
        try:
            if not limit:
                return db.session().query(Contacts).order_by(Contacts.contact_id.desc()).all()
            else:
                return db.session().query(Contacts).order_by(Contacts.contact_id.desc()).limit(limit).all()
        except Exception as ex:
            return None

    def add_contact(self, contact):
        try:
            session = db.session()
            session.add(contact)
            session.commit()
            return True
        except Exception as ex:
            db.session.rollback()
            return False
            # abort(500, ex.__str__())

    def update_contact(self, contact):
        try:
            session = db.session()
            session.query(Contacts).filter_by(contact_id=contact.contact_id) \
                .update(
                dict(name=contact.name,
                     phone=contact.phone,
                     address=contact.address
                     )
            )
            session.commit()
            return True
        except Exception as ex:
            db.session.rollback()
            abort(500, ex.__str__())

    def delete_contact(self, contact_id):
        try:
            session = db.session()
            obj = session.query(Contacts).filter_by(contact_id=contact_id).one()
            session.delete(obj)
            session.commit()
            return True
        except orm.exc.NoResultFound:
            db.session.rollback()
            return True
        except Exception as ex:
            db.session.rollback()
            return False
