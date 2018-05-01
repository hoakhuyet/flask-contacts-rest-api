from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS
import settings
from dbconnect import db
from contacts.contacts_api import bp_contact

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + settings.DB_PATH
db.init_app(app)

cors = CORS(app, resources={r"/contact-api/*": {"origins": "*"}})
app.register_blueprint(bp_contact, url_prefix="/contact-api")


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5008)
