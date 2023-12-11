from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Date, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///employees.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birthdate = Column(String)
    position = Column(String)
    salary = Column(Float)
    hire_date = Column(Date, default=datetime.now)

    def __init__(self, first_name, last_name, birthdate, position, salary, hire_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.position = position
        self.salary = salary
        self.hire_date = hire_date

    def __repr__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.birthdate} {self.position} {self.salary} {self.hire_date}"


Base.metadata.create_all(engine)
