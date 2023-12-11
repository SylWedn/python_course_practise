# -----------------------------------------------
# P.4.1
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

#------------------------1-------------------------
def sum_of_three_numbers(a, b, c):
    return a + b + c

print(sum_of_three_numbers(1, 2, 3))

# #----------------------2-------------------------
def function_2(nums):
    total = 0
    for num in nums:
        total += num
    return total
print(function_2([1, 1, 1, 1, 1, 1, 1, 1]))

#------------------------6-------------------------
def function_6(my_list):
    return list(set(my_list))

print(function_6([1, 1, 2, "dog", 3, 4, 4]))

#------------------------3-------------------------
def function_3(*args):
    return max(args)

print(function_3(1, 2, 3, 4))

#------------------------4-------------------------

def function_4(string):
    return string[::-1]

print(function_4("Aivaras"))


#------------------------5-------------------------

def function_5(string: str):
    numbers = []
    lower_case = []
    upper_case = []
    print("Count: ", len(string.split(" ")))
    for char in string:
        if char.isdigit():
            numbers.append(char)
        elif char.isupper():
            upper_case.append(char)
        elif char.islower():
            lower_case.append(char)
    return len(upper_case), len(lower_case), len(numbers)

print(function_5("13 AIVARAI 59 lol"))

#------------------------7-------------------------
def function_7(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(function_7(17))
print(function_7(33))

#------------------------8-------------------------


def function_8(string: str):
    word = string.split(" ")
    return word[::-1]

print(function_8("Python dog lol 13"))

#------------------------9-------------------------

def function_9(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(function_9(2000))
print(function_9(1900))
print(function_9(2016))
print(function_9(2013))

#------------------------10-------------------------
import datetime


def function_10(date: datetime.datetime):
    return (datetime.datetime.now() - date).total_seconds() / (60 * 60)


print(function_10(datetime.datetime.now() - datetime.timedelta(days=15)))

#---------------------------------------------------------------------------





