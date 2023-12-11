# -----------------------------------------------
# P.2.4
# -----------------------------------------------
# • Kauliukų žaidimas
#   • Sukurti programą, kuri:
#     • Sugeneruotų tris pseudo-atsitiktinius skaičius nuo 1 iki 6
#     • Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
#     • Kitu atveju atspausdinti „Laimėjai!“
#
# Patarimas: Naudoti while ciklą, funkciją random.randint (import random),
# else, break.
# -----------------------
# • A game of Dice
#   • Create a program which would:
#     • Generate three pseudorandom numbers from 1 to 6.
#     • If one of the numbers is 5, print "You lost..."
#     • Else, print "You won!"
#
# Tip: Use a while loop, function random.randint (import random), else, break.
# -----------------------------------------------

import random

numbers =[]

for _ in range (3):
    numbers.append(random.randint(1, 6))

for number in numbers:
    if number ==5:
        print("lost")
        break
else:
    print("won", numbers)
