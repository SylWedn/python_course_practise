# -----------------------------------------------
# P.DB7.3
# -----------------------------------------------
# • Sukurti banko sąskaitų programą.
#   Programa turi leisti įvesti asmenis, bankus ir sąskaitas, asmenims
#   priskirti sąskaitas bankuose (objektai: asmenys, bankai, sąskaitos) bei
#   išpildyti šiuos reikalavimus:
#     • Asmuo turi turėti vardą, pavardę, asmens kodą, telefono numerį.
#     • Bankas turi turėti pavadinimą, adresą, banko kodą, SWIFT kodą.
#     • Sąskaita turi turėti numerį, balansą, savininką (t.y. sąskaitai
#       priskirtą asmenį) ir banką.
#     • Asmuo gali turėti daug sąskaitų tiek tame pačiame, tiek skirtinguose
#       bankuose.
#     • Turi būti galimybė peržiūrėti vieno asmens visas sąskaitas ir jų
#       informaciją, pridėti arba nuimti pinigus iš kiekvienos jo sąskaitos.
#     • Turi būti galimybė bendrai peržiūrėti visus asmenis, bankus, sąskaitas
#       ir jų informaciją.
#     • Programa turi turėti komandinės eilutės interfeisą (angl. Command-Line
#       Interface (CLI)).
#   • Kartu su programa turi būti pridėta duomenų bazės schema.
# -----------------------
# English description will be added.
# -----------------------------------------------

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('sqlite:///database7_1.db')

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    f_name = Column('f_name', String(200))
    l_name = Column('l_name', String(200))
    p_code = Column('p_code', Integer)
    phone = Column('phone', Integer)
    accounts = relationship('Account', back_populates='account')


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    number = Column('number', String(200))
    balance = Column('balance', String(200))
    owner_id = Column('owner_id', Integer, ForeignKey('person.id'))
    bank_id = Column('bank_id', Integer, ForeignKey('bank.id'))
    person = relationship('Person', back_populates='person')
    banks = relationship('Bank', back_populates='bank')


class Bank(Base):
    __tablename__ = 'bank'
    id = Column(Integer, primary_key=True)
    title = Column('title', Integer)
    address = Column('address', String(300))
    bank_code = Column('bank_code', String(100))
    swift_code = Column('swift_code', Integer)
    accounts = relationship('Account', back_populates='account')


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
