import connexion
import six
from datetime import date
from sqlalchemy import or_

from swagger_server.models.sale import Sale  # noqa: E501
from swagger_server import util
from swagger_server.models import database
from swagger_server.models.database import db
from flask import current_app as app


def get_sale_by_id(id_):  # noqa: E501
    """Get sale by ID

     # noqa: E501

    :param id_: Customer ID
    :type id_: str

    :rtype: Sale
    """
    sale = db.session.query(database.Sale).filter_by(id=id_).scalar()
    if sale is None:
        return {}, 404
    return sale.to_model()


def get_sales(customer_id=None):  # noqa: E501
    """Get list of sales

    Get list of sales # noqa: E501

    :param customer_id: Customer ID
    :type customer_id: str

    :rtype: List[Sale]
    """
    filters = []
    if customer_id:
        filters.append(database.Sale.customer_id == customer_id)
    query = db.session.query(database.Sale).filter(*filters)
    return [p.to_model() for p in query]


def create_sale(body=None):  # noqa: E501
    """Create Sale

     # noqa: E501

    :param body: Sale object
    :type body: dict | bytes

    :rtype: Sale
    """
    if connexion.request.is_json:
        body = Sale.from_dict(connexion.request.get_json())  # noqa: E501
    # we disallow merge to ensure immutability
    # TODO all of this should become a procedure
    sale = database.Sale.from_model(body)

    # check salesperson is still active
    # it is okay if the sale is their last day of work
    salesperson_id = db.session.query(database.Salesperson.id).filter(
        database.Salesperson.id == sale.salesperson_id,
        or_(database.Salesperson.end_date == None, database.Salesperson.end_date <= sale.sale_date)
    ).scalar()
    if salesperson_id is None:
        return {"err": "Terminated salesperson cannot conduct sale"}, 400

    # select for update, start lock
    # we need at least one product in stock
    rows = db.session.query(database.Product).filter(
        database.Product.id == sale.product_id,
        database.Product.quantity >= sale.quantity,
    ).update(values={
        "quantity": database.Product.quantity - sale.quantity,
    })
    app.logger.debug(rows)
    if rows == 0:
        db.session.rollback()
        return {"err": "product not in stock"}, 400

    # TODO is there any other business logic stopping us from completing the sale?Ï
    db.session.add(sale)
    db.session.commit()
    return sale.to_model()
