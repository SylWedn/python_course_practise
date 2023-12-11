5# -----------------------------------------------
# P.2.2
# -----------------------------------------------
# • Parašyti programą, kuri:
#   • Leistų vartotojui įvesti skaičių.
#   • Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
#   • Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų
#     įvestų teigiamų skaičių sumą
#
# Patarimas: Naudoti ciklą while, sąlygą if, break
# -----------------------
# • Write a program which would:
#   • Ask a user to input a number.
#   • If the input number is positive, ask to input yet another number.
#   • If the input number is negative, quit the program and print the sum of all
#     input numbers.
#
# Tip: Use a while loop, an if condition and a break keyword.
# -----------------------------------------------

pos_num = []

while True:
    num = float(input("Enter num: "))
    if num >= 0 :
        pos_num.append(num)
    else:
        result = 0
        for pos_num in pos_num:
            result=result + pos_num
        print("result: ", result)
        break