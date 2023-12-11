import sqlite3
from lecture import Lecture
from methods import WorkWithDB


conn = sqlite3.connect('lectures.db')
c = conn.cursor()

lec = WorkWithDB()

lec.create_database('lectures.db')

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

