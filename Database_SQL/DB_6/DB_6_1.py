# -----------------------------------------------
# P.DB6.1
# -----------------------------------------------
# • Sukurti programą, kurioje:
#   • Būtų galima įvesti darbuotojus su šiais atributais:
#     • Vardas
#     • Pavardė
#     • Gimimo data
#     • Pareigos
#     • Atlyginimas
#     • Nuo kada dirba (data būtų nustatoma (apskaičiuojama) automatiškai,
#       panaudojant dabartinę datą).
#   • Duomenys būtų saugomi duomenų bazėje, panaudojant SQLAlchemy ORM
#     (Object–Relational Mapping), be SQL užklausų.
#   • Vartotojas su darbuotojų įrašais duomenų bazėje galėtų atlikti CRUD
#     operacijas (Create – įrašyti, Read – peržiūrėti, Update – atnaujinti,
#     Delete – ištrinti).
# -----------------------------------------------
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DB_6_1create_table import Employee

engine = create_engine('sqlite:///employees.db')
Session = sessionmaker(bind=engine)
session = Session()

while True:
    choice = int(input('Choose one of the following:\n1 - Show employees\n2 - Create employee\n3 - Update employee\n4 - Delete employee\n5 - Quit\n'))

    if choice == 1:
        employees = session.query(Employee).all()
        if employees:
            print('-----------------')
            for employee in employees:
                print(f'ID: {employee.id}, Name: {employee.first_name} {employee.last_name}, '
                      f'Birthdate: {employee.birthdate}, Position: {employee.position}, '
                      f'Salary: {employee.salary}, Hire date: {employee.hire_date}')
            print('-----------------')
        else:
            print('No employees found.')

    elif choice == 2:
        first_name1 = input('Enter first name: ')
        last_name1 = input('Enter last name: ')
        birthdate1 = input('Enter birthdate (YYYY-MM-DD): ')
        position1 = input('Enter position: ')
        salary1 = float(input('Enter salary: '))
        hire_date1 = datetime.now()

        new_employee = Employee(
            first_name=first_name1,
            last_name=last_name1,
            birthdate=birthdate1,
            position=position1,
            salary=salary1,
            hire_date=hire_date1
        )

        session.add(new_employee)
        session.commit()
        print('Employee added successfully.')

    elif choice == 3:
        employees = session.query(Employee).all()
        print('-----------------')
        for employee in employees:
            print(employee)
        print('-----------------')
        id_change = int(input('Choose an employee ID you want to update: '))
        changed_employee = session.query(Employee).filter_by(id=id_change).first()
        if changed_employee:
            print(f'Updating employee: {changed_employee.first_name} {changed_employee.last_name}')
            change = int(input('What do you want to update:\n1 - First name\n2 - Last name\n3 - Birthdate\n4 - Position\n5 - Salary\n'))
            if change == 1:
                changed_employee.first_name = input('Enter new first name: ')
            elif change == 2:
                changed_employee.last_name = input('Enter new last name: ')
            elif change == 3:
                changed_employee.birthdate = input('Enter new birthdate (YYYY-MM-DD): ')
            elif change == 4:
                changed_employee.position = input('Enter new position: ')
            elif change == 5:
                changed_employee.salary = float(input('Enter new salary: '))
            else:
                print('Invalid choice.')
                continue  # Continue the loop if the choice is invalid
            session.commit()
            print('Employee updated successfully.')
        else:
            print('Employee not found.')

    elif choice == 4:
        id_delete = int(input('Enter the ID of the employee to delete: '))
        deleted_employee = session.query(Employee).filter_by(id=id_delete).first()

        if deleted_employee:
            print(f'Deleting employee: {deleted_employee.first_name} {deleted_employee.last_name}')
            session.delete(deleted_employee)
            session.commit()
            print('Employee deleted successfully.')
        else:
            print('Employee not found.')

    elif choice == 5:
        print('Exiting the program.')
        break

    else:
        print('Invalid choice. Please select 1, 2, 3, 4, or 5.')

# Close the database connection when done
session.close()
