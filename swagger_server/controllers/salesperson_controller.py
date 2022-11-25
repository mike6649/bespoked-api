import logging
from decimal import Decimal
from typing import List

import connexion
import six
from sqlalchemy import or_, and_

from swagger_server.models.report import Report  # noqa: E501
from swagger_server.models.report_sale import ReportSale
from swagger_server.models.salesperson import Salesperson  # noqa: E501
from swagger_server import util
from swagger_server.models import database
from swagger_server import db
from flask import current_app as app
from datetime import date


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
    try:
        if connexion.request.is_json:
            body = Salesperson.from_dict(connexion.request.get_json())  # noqa: E501
        if not body:
            return {}, 400
        person = database.Salesperson.from_model(body)
        if person.end_date and person.begin_date > person.end_date:
            raise ValueError("Begin date cannot be after end date")
        db.session.merge(person)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return {"err": "Bad inputs, exc: {}".format(repr(e))}, 400
    return person.to_model()


def quarterly_report(id_, year, quarter):  # noqa: E501
    """Quarterly Report

     # noqa: E501

    :param id_: Salesperson ID
    :type id_: str
    :param year: Year
    :type year: str
    :param quarter: Quarter
    :type quarter: str

    :rtype: Report
    """

    def year_quarter_to_daterange(yr, qtr):
        if qtr == 1:
            b = date(yr, 1, 1)
            e = date(yr, 4, 1)
        elif qtr == 2:
            b = date(yr, 4, 1)
            e = date(yr, 7, 1)
        elif qtr == 3:
            b = date(yr, 7, 1)
            e = date(yr, 10, 1)
        else:
            b = date(yr, 10, 1)
            e = date(yr + 1, 1, 1)
        return b, e

    try:
        year = int(year)
        quarter = int(quarter)
    except:
        return {"err": "Bad inputs"}, 400
    if quarter not in range(1, 4 + 1):
        return {"err": "Not valid quarter"}, 400
    begin_date, end_date = year_quarter_to_daterange(year, quarter)

    salesperson = db.session.query(database.Salesperson).filter_by(id=id_).scalar()
    if salesperson is None:
        return {"err": "No salesperson"}, 404

    q = db.session.query(database.Sale, database.Discount.discount_pct).select_from(database.Sale).join(
        database.Discount,
        and_(
            database.Sale.product_id == database.Discount.product_id,
            database.Sale.sale_date.between(database.Discount.begin_date, database.Discount.end_date)
        ),
        isouter=True).filter(
        database.Sale.salesperson_id == id_,
        database.Sale.sale_date >= begin_date,
        database.Sale.sale_date < end_date,
    ).order_by(database.Sale.sale_date, database.Sale.product_id)

    sales: List[ReportSale] = []
    total_sales = Decimal(0)
    total_commission = Decimal(0)
    for sale, discount_pct in q:
        discount_rate = 1
        if discount_pct is not None:
            discount_rate = Decimal(1) - discount_pct / 100
        unit_price = sale.product.sale_price * discount_rate
        commission = unit_price * sale.product.commission_pct / 100 * sale.quantity
        total_sales += unit_price * sale.quantity
        total_commission += commission
        sales.append(ReportSale(
            id=sale.id,
            product=sale.product.to_model(),
            customer=sale.customer.to_model(),
            sale_date=sale.sale_date,
            quantity=sale.quantity,
            unit_price=str(unit_price),
            commission_pct=str(sale.product.commission_pct),
            commission=str(round(commission, 2))
        ))
    report = Report(
        salesperson=salesperson.to_model(),
        year=str(year),
        quarter=str(quarter),
        sales=sales,
        total_sales=str(round(total_sales, 2)),
        total_commission=str(round(total_commission, 2)),
    )

    return report
