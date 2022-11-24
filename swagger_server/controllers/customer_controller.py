import connexion
import six

from swagger_server.models.customer import Customer  # noqa: E501
from swagger_server import util
from swagger_server.models import database
from swagger_server.models.database import db
from flask import current_app as app


def get_customer_by_id(id_):  # noqa: E501
    """Get customer by ID

     # noqa: E501

    :param id_: Customer ID
    :type id_: str

    :rtype: Customer
    """
    customer = db.session.query(database.Customer).filter_by(id=id_).scalar()
    if customer is None:
        return {}, 404
    return customer.to_model()


def get_customers(firstname=None):  # noqa: E501
    """Get list of customers

    Get list of customers # noqa: E501

    :param firstname: First Name
    :type firstname: str

    :rtype: List[Customer]
    """
    filters = []
    if firstname:
        filters.append(database.Customer.firstname == firstname)
    query = db.session.query(database.Customer).filter(*filters)
    return [p.to_model() for p in query]


def update_customer(body=None):  # noqa: E501
    """Update or create Customer

     # noqa: E501

    :param body: Customer object
    :type body: dict | bytes

    :rtype: Customer
    """
    if connexion.request.is_json:
        body = Customer.from_dict(connexion.request.get_json())  # noqa: E501
    if not body:
        return {}, 400
    try:
        customer = database.Customer.from_model(body)
    except Exception as e:
        return {"err": "Bad inputs, exc: {}".format(repr(e))}, 400
    db.session.merge(customer)
    db.session.commit()
    return customer.to_model()
