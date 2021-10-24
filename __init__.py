from flask import Flask

from .models import db
from . import config

def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.app_context().push()
    flask_app.debug=True
    db.init_app(flask_app)
    if config.is_db == "True":
        db.create_all()

    return flask_app