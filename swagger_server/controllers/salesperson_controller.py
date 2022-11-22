import connexion
import six

from swagger_server.models.salesperson import Salesperson  # noqa: E501
from swagger_server import util


def get_salesperson(firstname=None):  # noqa: E501
    """Get list of salespersons

    Get list of salespersons # noqa: E501

    :param firstname: First Name
    :type firstname: str

    :rtype: List[Salesperson]
    """
    return 'do some magic!'


def get_salesperson_by_id(id):  # noqa: E501
    """Get salesperson by ID

     # noqa: E501

    :param id: Salesperson ID
    :type id: str

    :rtype: Salesperson
    """
    return 'do some magic!'


def update_sales_person(id, body=None):  # noqa: E501
    """Update or create salesperson

     # noqa: E501

    :param id: Salesperson ID
    :type id: str
    :param body: salesperson object
    :type body: dict | bytes

    :rtype: Salesperson
    """
    if connexion.request.is_json:
        body = Salesperson.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
