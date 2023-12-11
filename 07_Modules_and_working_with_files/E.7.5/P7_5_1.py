# -----------------------------------------------
# P.7.5
# -----------------------------------------------
# • Sukurti programą, kuri:
#   • Sukurtų klasę Darbuotojas su savybėmis Vardas, Pavardė, Atlyginimas.
#   • Inicijuoti kelis darbuotojų objektus ir išsaugoti juos faile su Pickle.
#   • Kitame faile nuskaityti objektus iš Pickle failo, ir atspausdinti visų jų
#     savybes (kitame faile galima nukopijuoti klasės kodą).
# -----------------------
# English description is in progress.
# -----------------------------------------------

import pickle


class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def __str__(self):
        return f'Name: {self.name} ' \
               f'\nSurname: {self.surname} ' \
               f'\nSalary: {self.salary}'

employee_list = [Employee("Antanas", "Antanaitis", 1000), Employee('Petras', 'Petraitis', 800), Employee('Jonas', 'Jonaitis', 8000)]


with open('employee_list.pkl', 'wb') as pickle_out:
    pickle.dump(employee_list, pickle_out)
