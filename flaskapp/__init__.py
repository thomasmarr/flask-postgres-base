from flask import Flask
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .main import main_blueprint
    from .error import error_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(error_blueprint)

    return app
