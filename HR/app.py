from flask import Flask
from flask_restful import Api
# from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import settings
from dbconnect import database
from users.users_endpoint import bp_users

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + settings.DB_PATH
database.init_app(app)

cors = CORS(app, resources={r"/hr-api/*": {"origins": "*"}})

app.register_blueprint(bp_users, url_prefix="/hr-api")

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True, port=5008)
