import logging

import connexion
import six
from sqlalchemy.orm import Query

from swagger_server.models.salesperson import Salesperson  # noqa: E501
from swagger_server import util
from swagger_server.models import database
from swagger_server import db
from flask import current_app as app


def get_salespersons(firstname=None):  # noqa: E501
    """Get list of salespersons

    Get list of salespersons # noqa: E501

    :param firstname: First Name
    :type firstname: str

    :rtype: List[Salesperson]
    """
    filters = []
    if firstname:
        app.logger.info(firstname)
        filters.append(database.Salesperson.firstname == firstname)
    query = db.session.query(database.Salesperson).filter(*filters)
    return [p.to_model() for p in query]


def get_salesperson_by_id(id_):  # noqa: E501
    """Get salesperson by ID

     # noqa: E501

    :param id_: Salesperson ID
    :type id_: str

    :rtype: Salesperson
    """
    person = db.session.query(database.Salesperson).filter_by(id=id_).scalar()
    if person is None:
        return {}, 404
    return person.to_model()


def update_sales_person(body=None):  # noqa: E501
    """Update or create salesperson

     # noqa: E501

    :param body: salesperson object
    :type body: dict | bytes

    :rtype: Salesperson
    """
    if connexion.request.is_json:
        body = Salesperson.from_dict(connexion.request.get_json())  # noqa: E501
    if not body:
        return {}, 400
    person = database.Salesperson.from_model(body)
    db.session.merge(person)
    db.session.commit()
    return person.to_model()
