import connexion
import six

from swagger_server.models.product import Product  # noqa: E501
from swagger_server import util


def get_product_by_id(id):  # noqa: E501
    """Get product by ID

     # noqa: E501

    :param id: Product ID
    :type id: str

    :rtype: Product
    """
    return 'do some magic!'


def get_products(purchase_price=None):  # noqa: E501
    """Get list of products

    Get list of products # noqa: E501

    :param purchase_price: Purchase Price
    :type purchase_price: str

    :rtype: List[Product]
    """
    return 'do some magic!'


def update_product(id, body=None):  # noqa: E501
    """Update or create product

     # noqa: E501

    :param id: Product ID
    :type id: str
    :param body: Product object
    :type body: dict | bytes

    :rtype: Product
    """
    if connexion.request.is_json:
        body = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
