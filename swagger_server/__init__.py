import logging

import connexion
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from swagger_server import encoder

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.config.from_envvar("CONFIG")
    print(app.app.config)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Bespoked Bikes - API'}, pythonic_params=True)
    db.init_app(app.app)

    return app
