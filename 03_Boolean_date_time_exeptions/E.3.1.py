# -----------------------------------------------
# P.3.1
# -----------------------------------------------
# • Parašyti programą, kuri:
#   • Leistų vartotojui įvesti sveiką skaičių.
#   • Atspausdinti True, jei skaičius teigiamas
#   • Atspausdinti False, jei skaičius neigiamas ar lygus 0
#   • True/False reikšmei išsaugoti naudoti boolean tipo kintamąjį
#     ar_skaicius_teigiamas
#
# Patarimas: naudoti input(), bool(), if/else
# -----------------------
# • Write a program which would:
#   • Ask a user to enter a whole number.
#   • Print True if the number is positive.
#   • Else, if the number is negative or zero, print False.
#   • Use a boolean type variable for storing a True/False logical value.
#
# Tip: use input(), bool(), if/else
# -----------------------------------------------

while True:
    try:
        num = int(input("Enter a whole number > "))
        break
    except ValueError:
        print("Error: you did not enter a whole number")

is_num_positive = bool()
#is_num_positive = False
#is_num_positive = 0


if num >0:
    is_num_positive =True
else:
    print(False)
