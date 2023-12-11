import sqlite3
from lecture import Lecture


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


conn = sqlite3.connect('lectures.db')
c = conn.cursor()

