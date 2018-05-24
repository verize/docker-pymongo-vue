from flask import current_app as app
from eve_swagger import swagger
from config.swagger_config import swagger_config


def init_swagger():
    app.register_blueprint(swagger)
    app.config['SWAGGER_INFO'] = swagger_config
    return swagger_config
