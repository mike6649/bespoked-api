import logging

import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from swagger_server import encoder

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    logging.basicConfig(level=logging.DEBUG)
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.config.from_envvar("CONFIG")
    CORS(app.app, resources={"*": {"origins": "*"}})
    print(app.app.config)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Bespoked Bikes - API'}, pythonic_params=True)
    db.init_app(app.app)

    return app
