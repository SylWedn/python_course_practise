# -----------------------------------------------
# P.2.6
# -----------------------------------------------
# • Perdaryti 5 užduotį taip, kad programa atspausdintų visus keliamuosius
#   metus, nuo 1900 iki 2100 metų.
#
# Keliamieji metai yra kas 4 metus, išskyrus paskutinius amžiaus metus, kurie
# keliamieji yra tik kas 400 metų.
# -----------------------
# • Refactor the program in the previous exercise (no. 5) so that it would
#   print all the leap years from 1900 to 2100.
#
# A leap year occurs every 4 years, except the first year of a century (ex.
# 2000) - it is a leap year if only it is divisible by 400 (which happens once
# every 400 years).
# -----------------------------------------------

start_year = 1900
end_year = 2100

print("Leap years from", start_year, "to", end_year, ":")

for year in range(start_year, end_year + 1):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year)