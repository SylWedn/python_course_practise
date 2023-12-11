# -----------------------------------------------
# P.DB6.3
# -----------------------------------------------
# • Patobulinti anksčiau sukurtą konsolės programą su automobilių įrašais,
#   naudojant SQLAlchemy.
#
# Duomenimis kol kas nereikia užpildyti, užtenka suvesti keletą įrašų ir
# patikrinti, ar veikia. Pirmiausia reikės susikurti ORM duomenų modelį, o jau
# tuomet parašyti programą, kuri galės vykdyti paiešką.
# -----------------------
# English description will be added.
# -----------------------------------------------

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DB_6_3_cars_table_creation import Cars

engine = create_engine('sqlite:///db6cars.db')
Session = sessionmaker(bind=engine)
session = Session()

while True:
    choice = int(input('Choose one of the following:\n1 - Show cars\n2 - Create car \n3 - Quit\n: '))

    if choice == 1:
        cars = session.query(Cars).all()
        if cars:
            print('-----------------')
            for car in cars:
                print(f'ID: {car.id}, Make: {car.make}, Model: {car.model}, Color: {car.color}, Year: {car.year}, Price: {car.price}')

            print('-----------------')
        else:
            print('No employees found.')

    elif choice == 2:
        make1 = input('Enter make: ')
        model1 = input('Enter model: ')
        color1 = input('Enter color: ')
        year1 = input('Enter year: ')
        price1 = float(input('Enter price: '))

        new_car = Cars(
            make=make1,
            model=model1,
            color=color1,
            year=year1,
            price=price1
        )

        session.add(new_car)
        session.commit()
        print('Car added successfully.')

    elif choice == 3:
        print('Exiting the program.')
        break

    else:
        print('Invalid choice. Please select 1, 2, 3')

session.close()
