
from flask_api import FlaskAPI
from flask import Flask


app = Flask(__name__)


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app.config[config_name])
    app.config.from_pyfile('config.py')

    return app
