import connexion
import six

from swagger_server.models.customer import Customer  # noqa: E501
from swagger_server import util


def get_customer_by_id(id):  # noqa: E501
    """Get customer by ID

     # noqa: E501

    :param id: Customer ID
    :type id: str

    :rtype: Customer
    """
    return 'do some magic!'


def get_customers(firstname=None):  # noqa: E501
    """Get list of customers

    Get list of customers # noqa: E501

    :param firstname: First Name
    :type firstname: str

    :rtype: List[Customer]
    """
    return 'do some magic!'


def update_customer(id, body=None):  # noqa: E501
    """Update or create Customer

     # noqa: E501

    :param id: Customer ID
    :type id: str
    :param body: Customer object
    :type body: dict | bytes

    :rtype: Customer
    """
    if connexion.request.is_json:
        body = Customer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
