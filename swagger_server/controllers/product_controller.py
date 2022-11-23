import connexion
import six

from swagger_server.models.product import Product  # noqa: E501
from swagger_server import util
from swagger_server.models import database
from swagger_server import db
from flask import current_app as app


def get_product_by_id(id_):  # noqa: E501
    """Get product by ID

     # noqa: E501

    :param id: Product ID
    :type id: str

    :rtype: Product
    """
    product = db.session.query(database.Product).filter_by(id=id_).scalar()
    if product is None:
        return {}, 404
    return product.to_dict()


def get_products():  # noqa: E501
    """Get list of products

    Get list of products # noqa: E501


    :rtype: List[Product]
    """
    return 'do some magic!'


def update_product(body=None):  # noqa: E501
    """Update or create product

     # noqa: E501

    :param body: Product object
    :type body: dict | bytes

    :rtype: Product
    """
    if connexion.request.is_json:
        body = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
