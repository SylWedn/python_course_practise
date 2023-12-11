from sqlalchemy import create_engine, Column, Integer, String, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
from DB6_3main import Cars
import csv

Base = declarative_base()

engine = create_engine('sqlite:///db6cars.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()



def insert_car_record(make, model, color, year, price):
    new_car = Cars(make=make, model=model, color=color, year=year, price=price)
    session.add(new_car)
    session.commit()

def insert_data_from_csv(csv_filename):
    try:
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                make = row['make']
                model = row['model']
                color = row['color']
                year = int(row['year'])
                price = int(row['price'])
                insert_car_record(make, model, color, year, price)
        print('Data from CSV file has been successfully inserted into the database.')
    except Exception as e:
        print(f'Error: {str(e)}')


#insert_data_from_csv("MOCK_DATA.csv")

def search_car_records(column_name, value, start_year, end_year, start_price, end_price):
    query = session.query(Cars)
    if start_year and end_year:
        query = query.filter(Cars.year.between(start_year, end_year))
    if start_price and end_price:
        query = query.filter(Cars.price.between(start_price, end_price))
    if value:
        query = query.filter(text(f"{column_name} = :value")).params(value=value)
    return query.all()


def show_menu():
    print('Select an option:')
    print('1. Add a new car record')
    print('2. Search for car records')
    print('3. Exit')


while True:
    show_menu()
    option = input('Enter an option: ')

    if option == '1':
        make = input('Enter the make: ')
        model = input('Enter the model: ')
        color = input('Enter the color: ')
        year = int(input('Enter the year: '))
        price = int(input('Enter the price: '))
        insert_car_record(make, model, color, year, price)
        print('The car record was added successfully.')

    elif option == '2':
        column_name = input('Enter the column name you are searching for: Make, Model, Color, Year or Price: ')
        value = input('Enter the value to search for (or leave empty): ')

        start_year = input('Enter the starting year (or leave empty): ')
        end_year = input('Enter the ending year (or leave empty): ')

        start_price = input('Enter the starting price (or leave empty): ')
        end_price = input('Enter the ending price (or leave empty): ')

        results = search_car_records(column_name, value, start_year, end_year, start_price, end_price)
        if results:
            print('Results:')
            for car in results:
                print(f'Make: {car.make}, Model: {car.model}, Color: {car.color}, Year: {car.year}, Price: {car.price}')
        else:
            print('No matching records found.')

    elif option == '3':
        break

    else:
        print('Invalid input.')

session.close()
