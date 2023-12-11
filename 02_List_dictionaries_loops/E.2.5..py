# -----------------------------------------------
# P.2.5
# -----------------------------------------------
# • Sukurti programą, kuri:
#   • Leistų vartotojui įvesti metus
#   • Atspausdintų „Keliamieji metai“, jei taip yra
#   • Atspausdintų „Nekeliamieji metai“, jei taip yra
# -----------------------
# • Create a program which would:
#   • Ask a user to enter a year.
#   • Print "Leap year", if that's the case.
#   • Else, print "Not a leap year".
# -----------------------------------------------


year = int(input("year:"))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is leap")
else:
    print(year, "not leap")
