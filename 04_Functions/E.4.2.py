# -----------------------------------------------
# P.4.2
# -----------------------------------------------

# 1. Sukurti funkciją, kuri patikrintų, ar paduotas Lietuvos piliečio asmens kodas
#    yra validus.
# 2. Padaryti, kad programa sugeneruotų teisingą asmens kodą (panaudojus anksčiau
#    sukurtą funkciją) pagal įvestą lytį, gimimo datą ir eilės numerį).
#
# Info apie asmens kodo sudarymą: https://lt.wikipedia.org/wiki/Asmens_kodas.
#
# Veikiantis validatorius/generatorius pavyzdys: https://www.runa.lt/useful/asmens_kodas.
# -----------------------
# 1. Create a function which would verify if the personal ID in the input is a
#    valid Lithuanian personal ID.
# 2. Generate a valid personal ID (using the function from the previous step)
#    using gender, birthdate and the serial number of your birth as inputs).
#
# Information on how personal IDs are created: https://lt.wikipedia.org/wiki/Asmens_kodas.
#
# Working personal ID validator and generator: https://www.runa.lt/useful/asmens_kodas.
# -----------------------------------------------

def valid_nin(national_number):

    if len(national_number) != 11:
        return False

    FM = int(national_number[0])
    year = int(national_number[1:3])
    month = int(national_number[3:5])
    day = int(national_number[5:7])


    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
