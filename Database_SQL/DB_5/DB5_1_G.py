import sqlite3

conn = sqlite3.connect('car.db')
cur = conn.cursor()

# Funkcija įterpia naują automobilio įrašą į duomenų bazę
def insert_car_record(make, model, color, year, price):
    query = 'INSERT INTO car (Make, Model, Color, Year, Price) VALUES (?, ?, ?, ?, ?)'
    cur.execute(query, (make, model, color, year, price))
    conn.commit()

# Funkcija ieško automobilių įrašų pagal nurodytus kriterijus
def search_car_records(columns, start_year, end_year, start_price, end_price):
    query = 'SELECT * FROM car WHERE '
    for column in columns:
        if column == 4:
            query += 'Year BETWEEN ? AND ? AND '
        elif column == 5:
            query += 'Price BETWEEN ? AND ? AND '
        else:
            query += '{} = ? AND '.format(COLUMN_NAMES[column])
    query = query[:-5]

    parameters = []
    if 4 in columns:
        parameters.append(start_year)
        parameters.append(end_year)
    if 5 in columns:
        parameters.append(start_price)
        parameters.append(end_price)

    cur.execute(query, parameters)
    return cur.fetchall()

# Funkcija rodo meniu vartotojui
def show_menu():
    print('Select an option:')
    print('1. Add a new car record')
    print('2. Search for car records')
    print('3. Exit')

# Pagrindinė programos dalis
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
        columns = []
        while True:
            column_number = input('Select a column to search by (enter 0 to exit): ')
            if column_number == '0':
                break
            column = int(column_number)
            if column in range(1, 6):
                columns.append(column)
            else:
                print('Invalid input.')

        start_year = None
        end_year = None
        start_price = None
        end_price = None

        if 4 in columns:
            start_year = input('Enter the starting year (YYYY): ')
            end_year = input('Enter the ending year (YYYY): ')
        if 5 in columns:
            start_price = input('Enter the starting price (USD): ')
            end_price = input('Enter the ending price (USD): ')

        results = search_car_records(columns, start_year, end_year, start_price, end_price)
        print('Results:')
        for row in results:
            print(row)

    elif option == '3':
        break

    else:
        print('Invalid input.')

conn.close()