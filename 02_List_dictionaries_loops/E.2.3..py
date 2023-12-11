5# -----------------------------------------------
# P.2.3
# -----------------------------------------------
# • Sukurti programą, kuri:
#   • Leistų vartotojui po vieną įvesti 5 žodžius
#   • Pridėtų įvestus žodžius į sąrašą
#   • Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
# • Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį
#
# Patarimas: Naudoti sąrašą (list), ciklą for, funkciją ar metodą len(), metodą
# index().
# -----------------------
# • Write a program which would:
#   • Ask a user to input 5 words, one word at a time.
#   • Store input words in a list.
#   • Print every word, its length and its index in a list (use 1-based indexing
#     in your output, i.e. where the first word's index is 1)
# • Advanced: modify a program to let a user input any number of words they choose.
#
# Tip: Use a list, for loop, a function or a method len(), a method index().
# -----------------------------------------------

words = []
word_count = int(input("word count: "))

for entry in range(word_count):
     word = input("Enter:")
     words.append(word)

for word in words:
    print(word, len(word), words.index(word) +1 )
