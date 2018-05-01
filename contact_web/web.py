from flask import Flask, current_app, redirect, url_for
from flask_cors import CORS
from contacts.contacts_view import bp_view_contact
from web_config import config

app = Flask(__name__)
app.config.from_object(config["development"])


cors = CORS(app, resources={r"/contacts/*": {"origins": "*"}})
app.register_blueprint(bp_view_contact, url_prefix="/contacts")


@app.route("/")
def hello():
    return redirect("/contacts")


if __name__ == "__main__":
    app.run(port=5009)
