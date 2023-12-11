# -----------------------------------------------
# P.7.4
# -----------------------------------------------
# • Sukurti naują projektą. Jame sukurti failą modulis.py, kuriame:
#   • Kintamajam kintamasis priskirti reikšmę „Čia yra kintamasis“
#   • Sukurti funkciją funkcija(), kuri atspausdina „Čia yra funkcija“.
#   • Sukurti klasę Klase taip, kad kai yra kuriami jos objektai, jų sukūrimo
#     momentu būtų atspausdinama „Čia yra klasės Klase objektas“.
# • Sukurti failą main.py, kuriame:
#   • Importuoti modulį modulis
#   • Atspausdinti importuotą kintamąjį kintamasis
#   • Paleisti importuotą funkciją funkcija()
#   • Sukurti importuotos klasės Klase objektą
# -----------------------
# • Create an ex_module.py file in which:
#   • Assign a variable ex_variable the value of "This is an example variable".
#   • Create a function ex_function() which would print "This is an example
#     function".
#   • Create a class ExObjectClass such that at the moment of the creation of
#     its objects, the following text would be printed: "This is an example
#     object".
# • Create a main.py file in which:
#   • Import the ex_module module.
#   • Print the value of the variable ex_variable from the imported module
#     ex_module.
#   • Call the function ex_function() from ex_module - it should print a text.
#   • Create an object of the class ExObjectClass from ex_module - a text
#     should be printed at the time of the object's creation.
# -----------------------------------------------

ex_variable = "This is an example variable"


def ex_function():
    print("This is an example function")


class ExObjectClass:
    def __str__(self):
        return "This is an example object"