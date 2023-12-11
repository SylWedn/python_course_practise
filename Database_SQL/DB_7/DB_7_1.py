# -----------------------------------------------
# P.DB7.1
# -----------------------------------------------
# • Naudojant SQLAlchemy, sukurti ORM duomenų modelį pagal duotą diagramą.
# (žr. diagramą https://i.imgur.com/82ZHe40.png)
#
# Kuriant many-to-many ryšį, galite naudoti arba Association Table,
#   (žr. teoriją https://docs.sqlalchemy.org/en/20/orm/basic_relationships
#   .html#many-to-many)
#   (žr. pavyzdį https://gist.github.com/00riddle00
#   /fd74fa409236f4227e259ad8d02f4f48)
#
# arba Association Object (t.y. sukurti tarpinei lentelei atskirą klasę).
#   (žr. teoriją https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#association-object)
#   (žr. pavyzdį https://gist.github.com/00riddle00
#   /62d465d80e66ca133ee7f80366496aa4)
#
# Jei naudosite Association Table, tai tarpinė lentelė susidarys tik iš
# dviejų stulpelių: „order_id“ ir „product_id“. Tuomet tarpinėje lentelėje
# stulpelių „id“ ir „quantity“ nenaudokite, programa gausis truputį
# paprastesnė, tačiau ne pilnai atitinkanti DB schemą. Tai gali būti kaip
# pirminis užduoties sprendimo variantas.
#
# Naudojant Association Object, tarpinėje lentelėje jau galima bus panaudoti
# papildomą stulpelį „id“ ir papildomą ryšio informaciją – stulpelį „quantity“.
# -----------------------
# English description will be added.
# -----------------------------------------------

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('sqlite:///database.db')

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    f_name = Column('f_name', String(200))
    l_name = Column('l_name', String(200))
    email = Column('email', String(170))


class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(80))


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(150))
    price = Column('price', Float)
    customer_orders = relationship('CustomerOrder', secondary='order_product', back_populates='products')
    customer_associations = relationship('OrderProduct', back_populates='product')


class CustomerOrder(Base):
    __tablename__ = 'customer_order'
    id = Column(Integer, primary_key=True)
    create_date = Column('create_date', String(30))
    customer_id = Column('customer_id', Integer, ForeignKey('customer.id'))
    status_id = Column('status_id', Integer, ForeignKey('status.id'))
    customer = relationship('Customer')
    status = relationship('Status')
    products = relationship('Product', secondary='order_product', back_populates='customer_orders')
    product_associations = relationship('OrderProduct', back_populates='customer_order')


class OrderProduct(Base):
    __tablename__ = 'order_product'
    id = Column(Integer, primary_key=True)
    order_id = Column('order_id', Integer, ForeignKey('customer_order.id'))
    product_id = Column('product_id', Integer, ForeignKey('product.id'))
    quantity = Column('quantity', Integer)
    customer_order = relationship('CustomerOrder', back_populates='product_associations')
    product = relationship('Product', back_populates='customer_associations')


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

session = sessionmaker(bind=engine)()

for c in range(5):
    customer = Customer(
        f_name=f'Customer First Name {c + 1}',
        l_name=f'Customer Last Name {c + 1}',
        email=f'customer{c + 1}@mail.com'
    )
    session.add(customer)
    session.commit()
customer = session.get(Customer, 2)
status = Status(name='Status 1')
product = Product(name='Product 1', price=12.5)

customer_order = CustomerOrder(
    create_date='2023-09-06',
    customer=customer,
    status=status
)
customer_order.products.append(product)

# order_product = OrderProduct(quantity=12)
# order_product.customer_order = customer_order
# order_product.product = product

session.add_all([customer, status, product, customer_order])
session.commit()

