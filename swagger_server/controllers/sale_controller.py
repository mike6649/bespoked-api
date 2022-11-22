import connexion
import six

from swagger_server.models.sale import Sale  # noqa: E501
from swagger_server import util


def get_sale_by_id(id):  # noqa: E501
    """Get sale by ID

     # noqa: E501

    :param id: Customer ID
    :type id: str

    :rtype: Sale
    """
    return 'do some magic!'


def get_sales(customer_id=None):  # noqa: E501
    """Get list of sales

    Get list of sales # noqa: E501

    :param customer_id: Customer ID
    :type customer_id: str

    :rtype: List[Sale]
    """
    return 'do some magic!'


def update_sale(body=None):  # noqa: E501
    """Create Sale

     # noqa: E501

    :param body: Sale object
    :type body: dict | bytes

    :rtype: Sale
    """
    if connexion.request.is_json:
        body = Sale.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
