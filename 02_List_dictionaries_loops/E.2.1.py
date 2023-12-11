# -----------------------------------------------
# P.2.1
# -----------------------------------------------
# • Sukurti norimą sąrašą ir žodyną ir juose:
#   • Atspausdinti vieną norimą įrašą
#   • Pridėti įrašą
#   • Ištrinti įrašą
#   • pakeisti įrašą
# • Išbandyti kitus sąrašų ir žodynų metodus (kaip funkcijos, tik susijusios su
#   kažkokia klase ar objektu) : clear(), index(), insert(), remove(), ...
#
# https://www.w3schools.com/python/python_ref_list.asp.
# https://www.w3schools.com/python/python_ref_dictionary.asp.
# -----------------------
# • Create a list and a dictionary (dict) with some data, and perform these actions:
#   • list: print a single element using its index; dict: print a single value
#     using its key.
#   • list: append a new element; dict: append a new key-value pair.
#   • list: remove an element; dict: remove a key-value pair.
#   • list: change some element's value; dict: change some value associated
#     with the key (use its key to change it).
# • Try out some other list and dictionary methods (methods are functions
#   associated with a class or an object): clear(), index(), insert(), remove(), ...
#
# https://www.w3schools.com/python/python_ref_list.asp.
# https://www.w3schools.com/python/python_ref_dictionary.asp.
# -----------------------------------------------

my_list = [ 1, 'two', 3.0, {"name": "John"}, 4]
print (my_list[1])
my_list.append(7)

print (my_list)
my_list.remove(3)
print (my_list)

my_list[3]=20
print (my_list)

my_list.remove(1)
element = my_list.pop(3)
print(element, my_list)


profile = {
    "name2" : "Sylvester",
    "info2" : {
        "age" : 30 ,
        "contact" : { "tel": "486456445", "email": "John@gmail.com", "adress" : "Vilnius"},
        "pets" : ["dog", "pig", "Gorilla"]


} }

profile["code"] ="3303"
print (profile.keys())
print(profile["name2"])

del profile["code"]


print(profile)

profile["info2"]["age"] = 16
print(profile)