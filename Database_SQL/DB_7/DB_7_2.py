# -----------------------------------------------
# P.DB7.2
# -----------------------------------------------
# • Parašyti programą, kuri, naudojantis 1 užduotyje sukurtu ORM duomenų
#   modeliu, sukurtų duomenų bazę ir leistų su ja atlikti šiuos veiksmus:
#   • Pridėti klientą.
#   • Pridėti produktą.
#   • Pridėti užsakymo statusą.
#   • Pridėti užsakymą.
#   • Peržiūrėti užsakymą pagal užsakymo ID.
#   • Pakeisti užsakymo statusą pagal užsakymo ID.
#   • Peržiūrėti visus kliento užsakymus, pagal kliento ID.
# -----------------------
# English description will be added.
# -----------------------------------------------

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('sqlite:///database7.db')

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    f_name = Column('f_name', String(200))
    l_name = Column('l_name', String(200))
    email = Column('email', String(170))

    def __str__(self):
        return f'{self.id} {self.f_name} {self.l_name} {self.email}'


class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(80))

    def __str__(self):
        return f'{self.id} {self.name}'


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(150))
    price = Column('price', Float)
    customer_orders = relationship('OrderProduct', back_populates='product')

    def __str__(self):
        return f'{self.id} {self.name} {self.price}'


class CustomerOrder(Base):
    __tablename__ = 'customer_order'
    id = Column(Integer, primary_key=True)
    create_date = Column('create_date', String(30))
    customer_id = Column('customer_id', Integer, ForeignKey('customer.id'))
    status_id = Column('status_id', Integer, ForeignKey('status.id'))
    customer = relationship('Customer')
    status = relationship('Status')
    products = relationship('OrderProduct', back_populates='customer_order')

    def __str__(self):
        return f'{self.id} {self.create_date} {self.customer_id} {self.status_id}'


class OrderProduct(Base):
    __tablename__ = 'order_product'
    id = Column(Integer, primary_key=True)
    order_id = Column('order_id', Integer, ForeignKey('customer_order.id'))
    product_id = Column('product_id', Integer, ForeignKey('product.id'))
    quantity = Column('quantity', Integer)
    customer_order = relationship('CustomerOrder', back_populates='products')
    product = relationship('Product', back_populates='customer_orders')


# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# customer1 = Customer(f_name="Antanas", l_name="Šampanas", email='sampanas@gmail.com')
# customer2 = Customer(f_name="Petras", l_name="Petraitis", email='ppetras@gmail.com')
#
# product1 = Product(name="Shampoo", price=8.50)
# product2 = Product(name="Soap", price=4.99)
#
# status1 = Status(name='completed')
# status2 = Status(name='declined')
#
# customer_order1 = CustomerOrder(create_date='2023-09-07', customer=customer1, status=status1)
# customer_order2 = CustomerOrder(create_date='2023-09-06', customer=customer2, status=status2)
#
# order_product1 = OrderProduct(quantity=3, customer_order=customer_order1, product=product1)
# order_product2 = OrderProduct(quantity=5, customer_order=customer_order2, product=product2)


def add_customer():
    name = input("Enter the customer's name: ")
    surname = input("Enter the customer's surname: ")
    email = input("Enter the customer's email: ")
    customer = Customer(f_name=f"{name}", l_name=f"{surname}", email=f'{email}')
    session.add(customer)
    session.commit()
    print("Customer added successfully.")


def add_product():
    name = input("Enter product's name: ")
    price = int(input("Enter product's price: "))
    product = Product(name=f"{name}", price=price)
    session.add(product)
    session.commit()
    print("Product added successfully.")


def add_customer_order():
    create_date = input("Enter the order date (YYYY-MM-DD): ")
    for customer in session.query(Customer).all():
        print(customer)
    customer_id = input('Enter customer Id: ')
    for status in session.query(Status).all():
        print(status)
    status_id = input('Enter status Id:')
    customer_order = CustomerOrder(
        create_date=create_date,
        customer=session.get(Customer, customer_id),
        status=session.get(Status, status_id)
    )
    session.add(customer_order)
    session.commit()
    print("Customer order added successfully.")


def add_order_product():
    quantity = int(input("Add quantity: "))
    for product in session.query(Product).all():
        print(product)
    product_id = input('Enter product Id: ')
    for customer_order in session.query(CustomerOrder).all():
        print(customer_order)
    customer_order_id = input('Enter order Id: ')
    order_product = OrderProduct(
        customer_order=session.get(CustomerOrder, customer_order_id),
        product=session.get(Product, product_id),
        quantity=quantity
    )
    session.add(order_product)
    session.commit()
    print("Order product added successfully.")


def add_status():
    status_name = input('Enter status name: ')
    status = Status(name=status_name)
    session.add(status)
    session.commit()
    print("Status added successfully.")


def view_order_by_order_id():
    id_num = int(input('Enter order id: '))
    order_list = []
    order = str(session.get(CustomerOrder, id_num))
    order_list.append(order)
    order_list = [word for line in order_list for word in line.split()]
    print(f'ID: {order_list[0]} \nDate: {order_list[1]} \nCustomer id: {order_list[2]} \nStatus id: {order_list[3]}')


def change_order_status():
    choose_id = int(input('Choose order id for which you want to change the status: '))
    current_order = session.get(CustomerOrder, choose_id)
    print(f'Current order status: {current_order.status.name}, all status options: ')
    for status in session.query(Status).all():
        print(status)
    new_status_id = input('Enter new status Id: ')
    current_order.status = session.get(Status, new_status_id)
    session.commit()


def view_orders_by_customer_id():
    search_id = input('Enter customer id: ')
    see_orders = session.query(CustomerOrder).filter_by(customer_id=search_id).all()
    for order in see_orders:
        print(order)


while True:
    user_input = int(input('What would you like to do? '
                           '\n(1) Add customer '
                           '\n(2) Add product '
                           '\n(3) Add customer order '
                           '\n(4) Add order product '
                           '\n(5) Add order Status '
                           '\n(6) View order by customer Id '
                           '\n(7) Change order status '
                           '\n(8) View order by order Id '
                           '\n(9) Quit \n> '))

    if user_input == 1:
        add_customer()
    elif user_input == 2:
        add_product()
    elif user_input == 3:
        add_customer_order()
    elif user_input == 4:
        add_order_product()
    elif user_input == 5:
        add_status()
    elif user_input == 6:
        view_order_by_order_id()
    elif user_input == 7:
        change_order_status()
    elif user_input == 8:
        view_orders_by_customer_id()
    elif user_input == 9:
        quit()
    else:
        print('Enter the number between 1 and 9')


