# -----------------------------------------------
# P.4.4
# -----------------------------------------------
# • Parašyti funkciją, kuri grąžintų kiekvieno elemento gretimą skaičių.
#
# Pvz.: Input: 5678, Output: 5 – 46, 6 – 57, 7 – 68, 8 - 79.
# -----------------------
# • Create a function which would return the two neighbor numbers of the input
#   number.
#
# Ex.: Input: 5678, Output: 5 – 46, 6 – 57, 7 – 68, 8 - 79.
# -----------------------------------------------


def function(number: int) -> str:
    string_number = str(number)
    output_list = []
    for digit in string_number
        output_list.append(f"{digit} - {int(digit) -1} {int(digit)}")

    return ", ".join(output_list)



