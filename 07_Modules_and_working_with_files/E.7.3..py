# P.7.3
# -----------------------------------------------
# • Python faile padaryti šiuos veiksmus (atskirai, ne iškart):
#   1. Importuoti modulį datetime. Atsispausdinti šiandienos datą ir laiką
#      kartu, tik datą (date.today()) bei tik laiką (.now().time()).
#   2. Iš paketo datetime importuoti modulį date. Atsispausdinti šiandienos datą.
#   3. Iš paketo datetime importuoti modulį date kaip data (as data).
#      Atspausdinti šiandienos datą.
# -----------------------
# • In a Python file (.py), perform these actions one by one:
#   1. Import datetime module and use it to print the current date and time
#      (datetime), then the date only (date.today()), and then the time only
#      (.now().time()).
#   2. From datetime module import date class and use it to print the current
#      date.
#   3. From datetime module import date class as ddaattee. Use it to print the
#      current date.
# -----------------------------------------------
import datetime
from datetime import date
from datetime import datetime as ddaattee

#1
current_datetime = datetime.datetime.now()
current_date = datetime.date.today()
current_time = datetime.datetime.now().time()

print("Current Date and Time:", current_datetime)
print("Current Date:", current_date)
print("Current Time:", current_time)

#2
current_date = date.today()
print("Current Date:", current_date)

#3
current_date = ddaattee.today()
print("Current Date:", current_date)