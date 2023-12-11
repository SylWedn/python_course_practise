# -----------------------------------------------
# P.4.3
# -----------------------------------------------
# • Sukurti funkciją, kuri grąžintų True reikšmę, jei įvesto skaičiaus pirma
#   skaitmenų pusė yra lygi antrąjai, priešingu atveju grąžintų False.
# -----------------------
# • Create a function which would return True if the input numbers digits' first
#   half is equal to the second half, and return False otherwise.
# -----------------------------------------------
def function(number: int) -> bool:
    string_number = str(number)
    if len(string_number) % 2 != 0:
        return False
    half = int(len(string_number) / 2)
    first_part = string_number[:half]
    second_part = string_number[half:]
    return first_part == second_part

print(function(1212))
print(function())