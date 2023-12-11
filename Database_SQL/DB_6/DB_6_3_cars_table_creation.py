from sqlalchemy import Column, Integer, String, Float, Date, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db6cars.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Cars(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    color = Column(String)
    year = Column(String)
    price = Column(Float)

    def __init__(self, make, model, color, year, price):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.make} {self.model} {self.color} {self.year} {self.price}"


Base.metadata.create_all(engine)