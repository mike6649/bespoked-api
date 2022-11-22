from sqlalchemy import Column, Integer, String, Numeric, BigInteger, Date, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    manufacturer = Column(String)
    style = Column(String)
    purchase_price = Column(Numeric(12, 2))
    sale_price = Column(Numeric(12, 2))
    quantity = Column(BigInteger)
    commission_pct = Column(Numeric(5, 2))


class Salesperson(Base):
    __tablename__ = 'salesperson'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    address = Column(String)
    phone = Column(String)
    begin_date = Column(Date)
    end_date = Column(Date)
    manager_id = Column(String)


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    address = Column(String)
    phone = Column(String)
    begin_date = Column(Date)

class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    salesperson_id = Column(Integer)
    sale_time = Column(TIMESTAMP)
    quantity = Column(Integer)

class Discount(Base):
    __tablename__ = 'discount'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    begin_date = Column(Date)
    end_date = Column(Date)
    discount_pct = Column(Numeric(4, 2))
