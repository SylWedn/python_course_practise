# -----------------------------------------------
# • Pakeisti 3 užduotį taip, kad neteisingai įvedus duomenis ar įvykus
#   klaidoms, programos mestų norimas klaidas lietuvių kalba (panaudoti
#   try/except)
# -----------------------
# • Modify the third program (exercise no. 3) so that when the input is not
#   valid, or any errors occur, the program would print the errors accordingly
#   (use try/except).
# ------------------------

import datetime

while True:
    try:
        date_string = input("Enter a date: (YYYY-MM=DD HH24:MI:SS")

        date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")


        print("1: ", round((datetime.datetime.now() - date).days / 365))
        print("2: ", round((datetime.datetime.now() - date).days / 30))
        print("4: ", round((datetime.datetime.now() - date).total_seconds() / (60 * 60 * 24)))
        print("5: ", round((datetime.datetime.now() - date).total_seconds() / (60*60)))
        print("5: ", round((datetime.datetime.now() - date).total_seconds() / 60))
        print("6: ", round((datetime.datetime.now() - date).total_seconds()))
        break
    except ValueError:
        print("enter not a valid date")
