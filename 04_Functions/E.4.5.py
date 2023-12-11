# -----------------------------------------------
# P.4.5
# -----------------------------------------------
# • Parašyti programą, kuri:
#   • Leistų vartotojui įvesti sumą, išleistą restorane.
#   • Turėtų funkciją, kuri prie sumos pridėtų mokesčius (21 proc. PVM).
#   • Turėtų funkciją, kuri prie sumos su PVM pridėtų arbatpinigius (15 proc.).
#
# Programa turėtų pridėti prie įvestos sumos mokesčius, arbatpinigius
# (panaudojant funkcijas) ir atspausdinti bendrą sumą.
# -----------------------
# • Write a program which would:
#   • Ask a user to enter the amount of money spent at a restaurant.
#   • Have a function which would add taxes to this amount (21 % VAT).
#   • Have a function which would add a tip (15 %) to the amount with the taxes
#     included.
#
# The program should print the total amount in the end.
# -----------------------------------------------

def add_vat(amount: float) -> float:
    return amount * 1.21

def add_tip(amount: float) -> float:
    return amount * 1.15

def add_item(amount:float):
    amount_with_vat = add_vat(amount)
    total_amount = add_tip(amount_with_vat)
    print("total", total_amount)

order = []

print("Enter item for your order")

while True:
    entered = input("enter ite amount:")
    if entered == "done":
        break
    amount_with_vat = add_vat(float(entered))
    total_amount = add_tip(amount_with_vat)
    order.append(total_amount)

print("total", round(sum(order), 3))