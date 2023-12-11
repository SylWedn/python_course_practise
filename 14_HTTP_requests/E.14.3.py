# -----------------------------------------------
# P.REQ.3
# -----------------------------------------------
# • Parašyti programą, kuri iš adreso https://orai.15min.lt/prognozes ištrauktų
#   ir atspausdintų oro prognozę Vilniuje šiuo metu. Galima naudoti string
#   metodus, RegEx.
# -----------------------
# English description will be added.
# -----------------------------------------------

import requests


def print_forecast():
    r = requests.get('https://orai.15min.lt/prognoze/vilnius')
    div_start_position = r.text.find('<div class="temperature alert-hot">')
    div_end_position = r.text.find('</div>', div_start_position)
    div = r.text[div_start_position:div_end_position + 6]
    temperature_start = div.find('</i>')
    temperature_end = div.find(str(div_end_position), temperature_start)
    temperature = div[temperature_start:temperature_end]
    print(temperature[10:-10])


print_forecast()
