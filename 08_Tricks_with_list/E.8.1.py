# -----------------------------------------------
# P.8.1
# -----------------------------------------------
# • Sukurti programą, kuri:
#   • Prie kiekvieno sakinio „The Zen of Python“ teksto žodžio pridėtų šauktuką
#     ir atspausdintų naują sakinį.
#
# Patarimas: Panaudoti map (su lambda) arba sąrašo apimtį (angl. list
# comprehension), " ".join().
# -----------------------
# • Create a program which would:
#   • Add an exclamation mark "!" to every word of a sentence "The Zen of
#     Python", and print the new sentence.
#
# Tip: Use map (with lambda) or list comprehension, " ".join().
# -----------------------------------------------
text = "The Zen of Python"


newtext = "".join(map(lambda word: word+"!", text.split()))
print(newtext)

newtext2 = "".join([word + "!" for word in text.split()])
print (newtext2)