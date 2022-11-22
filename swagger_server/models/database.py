from sqlalchemy import Column, Integer, String, Numeric, BigInteger, Date, TIMESTAMP
from swagger_server import models
from swagger_server import db


class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    manufacturer = Column(String)
    style = Column(String)
    purchase_price = Column(Numeric(12, 2))
    sale_price = Column(Numeric(12, 2))
    quantity = Column(BigInteger)
    commission_pct = Column(Numeric(5, 2))


class Salesperson(db.Model):
    __tablename__ = 'salesperson'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    address = Column(String)
    phone = Column(String)
    begin_date = Column(Date)
    end_date = Column(Date)
    manager = Column(String)

    # noinspection PyTypeChecker
    def to_model(self):
        return models.Salesperson(
            id=self.id,
            firstname=self.firstname,
            lastname=self.lastname,
            address=self.address,
            phone=self.phone,
            begindate=self.begin_date,
            enddate=self.end_date,
            manager=self.manager,
        )


class Customer(db.Model):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    address = Column(String)
    phone = Column(String)
    begin_date = Column(Date)

    # noinspection PyTypeChecker
    def to_model(self):
        return models.Customer(
            id=self.id,
            firstname=self.firstname,
            lastname=self.lastname,
            address=self.address,
            phone=self.phone,
            startdate=self.begin_date,
        )


class Sale(db.Model):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    salesperson_id = Column(Integer)
    sale_time = Column(TIMESTAMP)
    quantity = Column(Integer)

    # noinspection PyTypeChecker
    def to_model(self):
        return models.Sale(
            id=self.id,
            salesperson_id=self.salesperson_id,
            sales_date=self.sale_time,
        )


class Discount(db.Model):
    __tablename__ = 'discount'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    begin_date = Column(Date)
    end_date = Column(Date)
    discount_pct = Column(Numeric(4, 2))
