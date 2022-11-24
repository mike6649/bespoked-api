# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.report_sale import ReportSale  # noqa: F401,E501
from swagger_server.models.salesperson import Salesperson  # noqa: F401,E501
from swagger_server import util


class Report(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, salesperson: Salesperson=None, year: str=None, quarter: str=None, sales: List[ReportSale]=None, total_sales: str=None, total_commission: str=None):  # noqa: E501
        """Report - a model defined in Swagger

        :param salesperson: The salesperson of this Report.  # noqa: E501
        :type salesperson: Salesperson
        :param year: The year of this Report.  # noqa: E501
        :type year: str
        :param quarter: The quarter of this Report.  # noqa: E501
        :type quarter: str
        :param sales: The sales of this Report.  # noqa: E501
        :type sales: List[ReportSale]
        :param total_sales: The total_sales of this Report.  # noqa: E501
        :type total_sales: str
        :param total_commission: The total_commission of this Report.  # noqa: E501
        :type total_commission: str
        """
        self.swagger_types = {
            'salesperson': Salesperson,
            'year': str,
            'quarter': str,
            'sales': List[ReportSale],
            'total_sales': str,
            'total_commission': str
        }

        self.attribute_map = {
            'salesperson': 'salesperson',
            'year': 'year',
            'quarter': 'quarter',
            'sales': 'sales',
            'total_sales': 'total_sales',
            'total_commission': 'total_commission'
        }
        self._salesperson = salesperson
        self._year = year
        self._quarter = quarter
        self._sales = sales
        self._total_sales = total_sales
        self._total_commission = total_commission

    @classmethod
    def from_dict(cls, dikt) -> 'Report':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Report of this Report.  # noqa: E501
        :rtype: Report
        """
        return util.deserialize_model(dikt, cls)

    @property
    def salesperson(self) -> Salesperson:
        """Gets the salesperson of this Report.


        :return: The salesperson of this Report.
        :rtype: Salesperson
        """
        return self._salesperson

    @salesperson.setter
    def salesperson(self, salesperson: Salesperson):
        """Sets the salesperson of this Report.


        :param salesperson: The salesperson of this Report.
        :type salesperson: Salesperson
        """

        self._salesperson = salesperson

    @property
    def year(self) -> str:
        """Gets the year of this Report.


        :return: The year of this Report.
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year: str):
        """Sets the year of this Report.


        :param year: The year of this Report.
        :type year: str
        """

        self._year = year

    @property
    def quarter(self) -> str:
        """Gets the quarter of this Report.


        :return: The quarter of this Report.
        :rtype: str
        """
        return self._quarter

    @quarter.setter
    def quarter(self, quarter: str):
        """Sets the quarter of this Report.


        :param quarter: The quarter of this Report.
        :type quarter: str
        """

        self._quarter = quarter

    @property
    def sales(self) -> List[ReportSale]:
        """Gets the sales of this Report.


        :return: The sales of this Report.
        :rtype: List[ReportSale]
        """
        return self._sales

    @sales.setter
    def sales(self, sales: List[ReportSale]):
        """Sets the sales of this Report.


        :param sales: The sales of this Report.
        :type sales: List[ReportSale]
        """

        self._sales = sales

    @property
    def total_sales(self) -> str:
        """Gets the total_sales of this Report.


        :return: The total_sales of this Report.
        :rtype: str
        """
        return self._total_sales

    @total_sales.setter
    def total_sales(self, total_sales: str):
        """Sets the total_sales of this Report.


        :param total_sales: The total_sales of this Report.
        :type total_sales: str
        """

        self._total_sales = total_sales

    @property
    def total_commission(self) -> str:
        """Gets the total_commission of this Report.


        :return: The total_commission of this Report.
        :rtype: str
        """
        return self._total_commission

    @total_commission.setter
    def total_commission(self, total_commission: str):
        """Sets the total_commission of this Report.


        :param total_commission: The total_commission of this Report.
        :type total_commission: str
        """

        self._total_commission = total_commission
