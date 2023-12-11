# -----------------------------------------------
# P.DB1.2
# -----------------------------------------------
# • Sukurti programą, kuri:
#   • Sukurtų SQLite duomenų bazę.
#   • Sukurtų lentelę lectures su stulpeliais name, teacher, duration (duration
#     – trukmė minutėmis).
#   • Sukurtų keturias paskaitas:('Management', 'Kevin', 40), ('Python',
#     'Creed', 60), ('Java', 'Dwight', 80) ir ('RegEx', 'Toby', 90).
#   • Atspausdintų tik tas paskaitas, kurių trukmė didesnė nei 50 minučių.
#   • Atnaujintų paskaitos „Python“ pavadinimą į „Python Programming“.
#   • Ištrintų paskaitą, kurios dėstytojas – Toby.
#   • Atspausdintų visas paskaitas (visą lentelę).
# -----------------------
# English description will be added.
# -----------------------------------------------

import sqlite3

conn = sqlite3.connect("lectures.db")
c = conn.cursor()

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS
    lectures (
    Name text, 
    teacher text, 
    duration integer
    )""")

with conn:
     c.execute("INSERT INTO lectures values ('Management', 'Kevin', 40), "
               "('Python', 'Creed', 60), "
               "('Java', 'Dwight', 80), "
               "('RegEx', 'Toby', 90)")

with conn:
    c.execute("SELECT * FROM lectures where duration > 50")
    print(c.fetchall())

with conn:
    c.execute("update lectures set name='Python Programming' where name='Python'")

with conn:
    c.execute("delete from lectures where teacher='Toby'")

with conn:
    c.execute("SELECT * From lectures")
    print(c.fetchall())
