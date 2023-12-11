# -----------------------------------------------
# P.DB5.2
# -----------------------------------------------
# • Parašykite Python programą, kuri dirbtų su pirmoje užduotyje sukurta
#   automobilių duomenų baze, ir leistų vartotojui per konsolę:
#   • Įvesti naują automobilio įrašą.
#   • Ieškoti automobilių įrašų pagal kiekvieno stulpelio reikšmes.
#
# Vartotojas gali pasirinkti, kuriuos stulpelius paieškoje praleisti. Metus ir
# kainą vartotojas turėtų nurodyti formatu (nuo ... iki ...).
# -----------------------
# English description will be added.
# -----------------------------------------------

# -----------------------------------------------
# P.DB5.2
# -----------------------------------------------
# • Parašykite Python programą, kuri dirbtų su pirmoje užduotyje sukurta
#   automobilių duomenų baze, ir leistų vartotojui per konsolę:
#   • Įvesti naują automobilio įrašą.
#   • Ieškoti automobilių įrašų pagal kiekvieno stulpelio reikšmes.
#
# Vartotojas gali pasirinkti, kuriuos stulpelius paieškoje praleisti. Metus ir
# kainą vartotojas turėtų nurodyti formatu (nuo ... iki ...).
# -----------------------
# English description will be added.
# -----------------------------------------------

import sqlite3

conn = sqlite3.connect('db5cars.db')
cur = conn.cursor()

COLUMN_NAMES = ['ID', 'Make', 'Model', 'Color', 'Year', 'Price']

def insert_car_record(make, model, color, year, price):
    query = 'INSERT INTO car (Make, Model, Color, Year, Price) VALUES (?, ?, ?, ?, ?)'
    cur.execute(query, (make, model, color, year, price))
    conn.commit()

def search_car_records(column_name, value, start_year, end_year, start_price, end_price):
    query = 'SELECT * FROM car WHERE {} '.format(column_name)

    parameters = []

    if start_year and end_year:
        query += 'AND Year BETWEEN ? AND ? '
        parameters.extend([start_year, end_year])
    if start_price and end_price:
        query += 'AND Price BETWEEN ? AND ? '
        parameters.extend([start_price, end_price])

    if value:
        query += '= ? '
        parameters.append(value)

    cur.execute(query, parameters)
    return cur.fetchall()

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
        year = input('Enter the year: ')
        price = input('Enter the price: ')
        insert_car_record(make, model, color, year, price)
        print('The car record was added successfully.')

    elif option == '2':
        print('Select a column to search by:')
        for i, column_name in enumerate(COLUMN_NAMES[1:], start=1):
            print(f'{i}. {column_name}')

        column_number = int(input('Enter the column number: '))
        if column_number in range(1, len(COLUMN_NAMES)):
            selected_column = COLUMN_NAMES[column_number]
            value = input(f'Enter the value for {selected_column} (or leave empty): ')

            start_year = None
            end_year = None
            start_price = None
            end_price = None

            if 'Year' in selected_column:
                start_year = input('Enter the starting year (YYYY): ')
                end_year = input('Enter the ending year (YYYY): ')
            if 'Price' in selected_column:
                start_price = input('Enter the starting price (USD): ')
                end_price = input('Enter the ending price (USD): ')

            results = search_car_records(selected_column, value, start_year, end_year, start_price, end_price)
            print('Results:')
            for row in results:
                print(row)
        else:
            print('Invalid input.')

    elif option == '3':
        break

    else:
        print('Invalid input.')

conn.close()