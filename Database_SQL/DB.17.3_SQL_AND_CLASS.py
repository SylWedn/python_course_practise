# -----------------------------------------------
# P.DB1.3
# -----------------------------------------------
# • Perdaryti 2 užduoties programą taip, kad ji:
#   • Sukurtų fizinę SQLite duomenų bazę (faile).
#   • Turėtų klasę Lecture su atributais name, teacher ir duration.
#   • Tas pačias keturias paskaitas paduotų į duomenų bazę kaip klasės Lecture
#     objektus, ir išsaugotų juos kaip keturis duomenų bazės įrašus.
# -----------------------
# English description will be added.
# -----------------------------------------------
import sqlite3

conn = sqlite3.connect("lectures1.db")
c = conn.cursor()

class Lecture:
    def __init__(self, name, teacher, duration):
        self.name = name
        self.teacher = teacher
        self.duration = duration

        c.execute("""CREATE TABLE IF NOT EXISTS lectures1 (
                     name TEXT,
                     teacher TEXT,
                     duration INTEGER)""")
        conn.commit()

        self.insert_into_db()

    def insert_into_db(self):
        c.execute("INSERT INTO lectures1 (name, teacher, duration) VALUES (?, ?, ?)",
                  (self.name, self.teacher, self.duration))
        conn.commit()

lectures_data = [
    ('Management', 'Kevin', 40),
    ('Python', 'Creed', 60),
    ('Java', 'Dwight', 80),
    ('RegEx', 'Toby', 90)
]

for lecture_data in lectures_data:
    lecture = Lecture(*lecture_data)

conn.close()

