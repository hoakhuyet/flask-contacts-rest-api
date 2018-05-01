from flask import Blueprint, render_template, current_app, url_for, redirect, session, request, flash
from .contacts_common import ContactCommon

bp_view_contact = Blueprint('contact_web', __name__)


@bp_view_contact.route("/index")
def index():
    common = ContactCommon(current_app.config["API_URL"])
    data = common.get_all_contact(current_app.config["CONTACT_URI"])
    return render_template("contacts/index.html", data=data)


@bp_view_contact.route("/")
def contacts():
    common = ContactCommon(current_app.config["API_URL"])
    data = common.get_all_contact(current_app.config["CONTACT_URI"])
    return render_template("contacts/index.html", data=data)


@bp_view_contact.route("/update/<int:contact_id>")
def update(contact_id):
    common = ContactCommon(current_app.config["API_URL"])
    uri = "{}/{}".format(current_app.config["CONTACT_URI"], contact_id)
    data = common.get_contact(uri)
    if not data:
        return redirect("/contacts")
    else:
        session["update"] = contact_id
        return render_template("contacts/update.html", data=data)


@bp_view_contact.route("/add")
def add():
    return render_template("contacts/add.html")


@bp_view_contact.route("/delete/<int:contact_id>")
def delete(contact_id):
    common = ContactCommon(current_app.config["API_URL"])
    uri = "{}/{}".format(current_app.config["CONTACT_URI"], contact_id)
    data = common.get_contact(uri)
    if not data:
        return redirect("/contacts")
    else:
        session["delete"] = contact_id
        return render_template("contacts/delete.html", data=data)


@bp_view_contact.route("/deletecontact", methods=["POST"])
def deletecontact():
    if request.method == "POST" and request.form["delete"]:
        contact_id = session["delete"]
        common = ContactCommon(current_app.config["API_URL"])
        uri = "{}/{}".format(current_app.config["CONTACT_URI"], contact_id)
        print(uri)
        if common.delete_contact(uri):
            flash("A phone number has been deleted")
        else:
            flash("A phone number can not be deleted")
        #
        # response = requests.delete(url, data=json.dumps(payload), headers=headers,
        #                            auth=HTTPBasicAuth(toggl_token, 'api_token'))
        return redirect("/contacts")
