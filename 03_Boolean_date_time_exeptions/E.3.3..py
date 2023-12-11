# -----------------------------------------------
# P.3.3
# -----------------------------------------------
# • Parašyti programą, kuri:
#   • Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
#   • Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
#     1. Metų
#     2. Mėnesių
#     3. Dienų
#     4. Valandų
#     5. Minučių
#     6. Sekundžių
# • Kadangi tiksliai galima paskaičiuoti tik dienas ir sekundes, metus,
#   mėnesius ir t.t. paskaičiuokite apytiksliai.
#
# Patarimas: naudoti datetime, .days(), .total_seconds()
#
# Skaičių suapvalinimo pavyzdys (kurio gali prireikti šioje užduotyje):
#     skaicius = 4.66
#     print(round(skaicius))
# -----------------------
# • Write a program which would:
#   • Let a user enter a date and time (ex. his birthdate)
#   • Calculate and print how many of the following have passed since that date
#     and time:
#     1. Years
#     2. Months
#     3. Days
#     4. Hours
#     5. Minutes
#     6. Seconds
# • Since only days and seconds can be counted exactly, count the years,
#   months, hours and minutes approximately.
#
# Tip: use datetime, .days(), .total_seconds()
#
# Example of rounding a number (which can be useful in this exercise):
#     number = 4.66
#     print(round(number))
# -----------------------------------------------


import datetime

date_string = input("Enter a date: (YYYY-MM=DD HH24:MI:SS")
date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

print(type(date_string), type(date))

print("1: ", round((datetime.datetime.now() - date).days / 365))
print("2: ", round((datetime.datetime.now() - date).days / 30))
print("3: ", round((datetime.datetime.now() - date).days))
print("4: ", round((datetime.datetime.now() - date).total_seconds / (60 * 60 * 24)))
print("5: ", round((datetime.datetime.now() - date).total_seconds() / 60))
print("6: ", round((datetime.datetime.now() - date).total_seconds()))
