
# P.4.1
# -----------------------------------------------
# • Sukurkite ir išsibandykite funkcijas, kurios:
#   1. Grąžintų trijų paduotų skaičių sumą.
#   2. Grąžintų paduoto sąrašo iš skaičių, sumą.
#   3. Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).
#   4. Grąžintų paduotą string atbulai.
#   5. Atspausdintų, kiek paduotame string yra žodžių, didžiųjų ir mažųjų
#      raidžių, skaičių.
#   6. Grąžintų sąrašą tik su unikaliais paduoto sąrašo elementais.
#   7. Grąžintų, ar paduotas skaičius yra pirminis.
#   8. Išrikiuotų paduoto string žodžius nuo paskutinio iki pirmojo.
#   9. Grąžina, ar paduoti metai yra keliamieji, ar ne.
#   10. Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų,
#       valandų, minučių, sekundžių.
# -----------------------
# • Create the functions (and try them out) which would:
#   1. Return a sum of three input numbers.
#   2. Return a sum of the numbers from the input list.
#   3. Print the greatest number out of several input numbers (using *args).
#   4. Return an input string in reverse.
#   5. From the input string, print how many words, uppercase and lowercase
#      letters and numbers it has.
#   6. Return a list containing only unique elements from the input list.
#   7. Return a True/False value whether an input number is prime.
#   8. Sort the words of an input string from the first to the last.
#   9. Return a True/False value whether the input year (a number) is a leap
#      year or not.
#   10. Print how many years, months, days, hours, minutes and seconds have
#       passed since the input date and time.
# -----------------------------------------------







def function_1(number0, number1, number2):
    return number0 + number1 + number2

print(function_1(1,1,1))

def function_2(numbers):
    total = 0
    for number in numbers:
        total += number

    return total

print (function_2([1,1,1,1,1,1,1,1,1]))


def function_3(*args):
    return max(args)
print(function_3(1,3,4,5,6,2,3,5,6,-12,-15))

def function_4(string):
    return string[::-1]

print(function_4("python"))

def function_5(string: str):
    numbers = []
    lower_case = []
    upper_case = []
    print("word count", len(string.split(" ")))
    for character in string:
        if character.isdigit():
            numbers.append(character)
        elif character.isupper():
            upper_case=character
        elif character.islower():
            lower_case = character
    print("Upper: ", len(upper_case))
    print("Lower: ", len(upper_case))
    print("Numbers: ", len(upper_case))

function_5("word 1 cat 22 , . sky Python")







def function_6(my_list):
    return (set(my_list))

print(function_6([1,1,2,"cat",2,3]))

def function_7(number: int) -> bool:
    for i in range(2, number):
        if number % i ==0:
            return False
    return True

print(function_7(17))
print(function_7(31))

def function_8(string: str):
    words = string.split(" ")
    print(words[::-1])

function_8("Python cat sky 123")




def function_9(year: int) -> bool:
    if year %400 ==0:
        return True
    elif year % 100 == 0:
        return False
    elif year %4 == 0:
        return True

    return False





