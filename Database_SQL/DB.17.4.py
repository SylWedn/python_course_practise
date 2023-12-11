# -----------------------------------------------
# P.DB1.4
# -----------------------------------------------
# • Perdaryti 3 užduoties programą taip, kad visi veiksmai su duomenų baze būtų
#   atliekami naujoje klasėje, skirtoje dirbti su duomenų baze. Kiekvieną iš
#   žemiau užrašytų funkcionalumų turi įgyvendinti atskiras šios klasės
#   metodas:
#   • Naujos lentelės sukūrimas.
#   • Klasės Lecture objekto įrašymas į duomenų bazę (kaip naujo duomenų bazės
#     įrašo).
#   • Paskaitos suradimas duomenų bazėje pagal pavadinimą.
#   • Norimos paskaitos trukmės pakeitimas duomenų bazėje.
#   • Norimos paskaitos ištrynimas duomenų bazėje.
#   • Visų paskaitų (t.y. visos lentelės) atvaizdavimas.
# -----------------------
# English description will be added.
# -----------------------------------------------

import sqlite3


class Lecture:
    def __init__(self, name, teacher, duration):
        self.name = name
        self.teacher = teacher
        self.duration = duration

class WorkWithDB:

    def create_database(self, db_name):
        with conn:
            c.execute(f"""CREATE TABLE IF NOT EXISTS
                lectures (
                Name TEXT,
                teacher TEXT,
                duration INT
                )""")
        print(f'Database {db_name} has been created')

    def insert_info(self, lecture: Lecture):
        with conn:
            c.execute(f"INSERT INTO lectures VALUES ('{lecture.name}', '{lecture.teacher}', '{lecture.duration}')")
        print('Data inserted successfully')

    def find_name(self, find_lecture):
        with conn:
            c.execute(f"SELECT * FROM lectures WHERE Name='{find_lecture}'")
            print(c.fetchall())

    def update_duration(self, lecture_name, update_dur):
        with conn:
            c.execute(f"UPDATE lectures SET duration='{update_dur}' WHERE Name='{lecture_name}'")
            print('Duration updated successfully')

    def delete_lecture(self, del_lec):
        with conn:
            c.execute(f"DELETE FROM lectures WHERE Name='{del_lec}'")
            print('Line deleted successfully')

    def show_all(self):
        with conn:
            c.execute("SELECT * FROM lectures")
            print(c.fetchall())


custom_db_name = input('Enter the name of your database: ')

conn = sqlite3.connect(custom_db_name)
c = conn.cursor()

lec = WorkWithDB()

lec.create_database(custom_db_name)

lec.insert_info(Lecture('Management', 'Kevin', 40))
lec.insert_info(Lecture('Python', 'Creed', 60))
lec.insert_info(Lecture('Java', 'Dwight', 80))
lec.insert_info(Lecture('RegEx', 'Toby', 90))
lec.find_name('Management')
lec.update_duration('Python', 75)
lec.delete_lecture('Java')
lec.show_all()

conn.commit()
conn.close()
