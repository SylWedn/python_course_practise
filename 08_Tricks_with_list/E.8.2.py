# -----------------------------------------------
# P.8.2
# -----------------------------------------------
# • Sukurti programą, kuri:
#   • Sukurtų sąrašą iš skaičių nuo 0 iki 50
#   • Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
#   • Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
#   • Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų
#   • Su kvadratų sąrašu atliktų šiuos veiksmus: atspausdintų sumą, mažiausią
#     ir didžiausią skaičių, vidurkį, medianą
#   • Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai
#
# Patarimas: Naudoti map, filter arba list comprehension, sum, min, max, %,
# mean, median (from statistics import mean, median).
# -----------------------
# • Create a program which would:
#   • Create a list of numbers from 0 to 50.
#   • Multiply every number in a list by 10 and print the resulting list.
#   • Print only the list of numbers from the original list which are divisible
#     by 7.
#   • Square (i.e. raise to the power of 2) every number in a list and print
#     the resulting list of squares.
#   • Print some statistical information about this list of squares: the sum of
#     its elements, minimum and maximum number, mean and median.
#   • Sort this list of squares in ascending order, and then print the
#     resulting list in reverse (i.e. in descending order).
#
# Tip: Use map, filter or list comprehension, sum, min, max, %, mean, median
# (from statistics import mean, median).
# -----------------------------------------------
from statistics import mean, median

num = list(range(51))

mlist = map(lambda x: x * 10, num)

print(list(mlist))

div7 = filter(lambda x: x % 7 == 0, num)

print(list(div7))

pow_list = list(map(lambda x: x ** 2, num))

print(pow_list)

print(sum(pow_list))
print(min(pow_list))
print(max(pow_list))
print(round(mean(pow_list), 2))
print(median(pow_list))

print("-" * 20)

new_pow_list = sorted(pow_list, reverse=True)
print(new_pow_list)

# sum_list = map(lambda x: sum(x), pow_list)
# print(list(pow_list))
