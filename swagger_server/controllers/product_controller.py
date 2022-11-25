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

    :param id_: Product ID
    :type id_: str

    :rtype: Product
    """
    product = db.session.query(database.Product).filter_by(id=id_).scalar()
    if product is None:
        return {}, 404
    return product.to_model()


def get_products():  # noqa: E501
    """Get list of products

    Get list of products # noqa: E501


    :rtype: List[Product]
    """
    query = db.session.query(database.Product)
    return [p.to_model() for p in query]


def update_product(body=None):  # noqa: E501
    """Update or create product

     # noqa: E501

    :param body: Product object
    :type body: dict | bytes

    :rtype: Product
    """

    try:
        if connexion.request.is_json:
            body = Product.from_dict(connexion.request.get_json())  # noqa: E501
        if not body:
            return {}, 400
        product = database.Product.from_model(body)
        if product.sale_price <= 0 or product.purchase_price <= 0:
            raise ValueError("Price must be postive")
        db.session.merge(product)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return {"err": "Bad inputs, exc: {}".format(repr(e))}, 400

    return product.to_model()
