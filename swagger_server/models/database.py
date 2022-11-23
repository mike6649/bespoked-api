from decimal import Decimal

from sqlalchemy import Column, Integer, String, Numeric, BigInteger, Date, TIMESTAMP
from swagger_server import models
from swagger_server import db


class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    manufacturer = Column(String)
    style = Column(String)
    purchase_price = Column(Numeric(12, 2))
    sale_price = Column(Numeric(12, 2))
    quantity = Column(BigInteger)
    commission_pct = Column(Numeric(5, 2))

    # noinspection PyTypeChecker
    def to_model(self):
        return models.Product(
            id=self.id,
            name=self.name,
            manufacturer=self.manufacturer,
            style=self.style,
            purchase_price=str(self.purchase_price),
            sale_price=str(self.sale_price),
            quantity=self.quantity,
            commission_pct=str(self.commission_pct),
        )

    @classmethod
    def from_model(cls, model: models.Product):
        product = cls()
        if model.id is not None:
            product.id = model.id
        product.name = model.name
        product.manufacturer = model.manufacturer
        product.style = model.style
        product.purchase_price = Decimal(model.purchase_price)
        product.sale_price = Decimal(model.sale_price)
        product.quantity = model.quantity
        product.commission_pct = Decimal(model.commission_pct)
        return product


class Salesperson(db.Model):
    __tablename__ = 'salesperson'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String)
    lastname = Column(String)
    address = Column(String)
    phone = Column(String)
    begin_date = Column(Date)
    end_date = Column(Date)
    manager = Column(String)

    @classmethod
    def from_model(cls, salesperson: models.Salesperson):
        person = cls()
        if salesperson.id is not None:
            person.id = salesperson.id
        person.firstname = salesperson.firstname
        person.lastname = salesperson.lastname
        person.address = salesperson.address
        person.phone = salesperson.phone
        person.begin_date = salesperson.begin_date
        person.end_date = salesperson.end_date
        person.manager = salesperson.manager
        return person

    # noinspection PyTypeChecker
    def to_model(self):
        return models.Salesperson(
            id=self.id,
            firstname=self.firstname,
            lastname=self.lastname,
            address=self.address,
            phone=self.phone,
            begin_date=self.begin_date,
            end_date=self.end_date,
            manager=self.manager,
        )


class Customer(db.Model):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
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
            begin_date=self.begin_date,
        )

    @classmethod
    def from_model(cls, model: models.Customer):
        customer = cls()
        if model.id is not None:
            customer.id = model.id
        customer.firstname = model.firstname
        customer.lastname = model.lastname
        customer.address = model.address
        customer.phone = model.phone
        customer.begin_date = model.begin_date
        return customer


class Sale(db.Model):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer)
    customer_id = Column(Integer)
    salesperson_id = Column(Integer)
    sale_date = Column(Date)
    quantity = Column(Integer)

    # noinspection PyTypeChecker
    def to_model(self):
        return models.Sale(
            id=self.id,
            salesperson_id=self.salesperson_id,
            sale_date=self.sale_date,
            quantity=self.quantity,
            product_id=self.product_id,
            customer_id=self.customer_id,
        )

    @classmethod
    def from_model(cls, model: models.Sale):
        sale = cls()
        if model.id is not None:
            sale.id = model.id
        sale.salesperson_id = model.salesperson_id
        sale.sale_date = model.sale_date
        sale.quantity = model.quantity
        sale.product_id = model.product_id
        sale.customer_id = model.customer_id
        return sale


class Discount(db.Model):
    __tablename__ = 'discount'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer)
    begin_date = Column(Date)
    end_date = Column(Date)
    discount_pct = Column(Numeric(4, 2))
