# -----------------------------------------------
# P.WEB.1
# -----------------------------------------------
# • Parašyti programą, kuri nuskaitytų naujienų portalo Delfi antraštes, ir:
#   • Atrinktų tik tas antraštes, kurios turi dvitaškį.
#   • Sudėtų antraščių dalis iki dvitaškio į vieną sarašą (pirmajį), o dalis po
#     dvitaškio – į kitą sąrašą (antrąjį).
#   • Išmaišytų antrąjį sąrašą.
#   • Atspausdintų antraščių dalis iš pirmojo sarašo ir prie jų prijungtų
#     antraščių dalis iš antrojo sąrašo. Turėtų gautis panašus rezultatas į:
#     • „Orai: už 9 šlakius teks sumokėti 26 tūkstančius eurų“
#     • „Antradienio vakare kauniečius išgąsdino termofikacijos elektrinė: ar
#       bus naujagimių bumas?“
# • Sukurti blogų žodžių sąrašą, pagal kurį išsifiltruoja pranešimai apie
#   COVID, mirtis ir t.t., ir pagal tai išfiltruoti antraštes (ankstyvoje
#   stadijoje, kol dar antraštės neperskirtos ir nesudėtos į atskirus sąrašus).
# -----------------------
# English description will be added.
# -----------------------------------------------

from bs4 import BeautifulSoup
import requests
import random


source = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(source, 'html.parser')
headlines = [headlines.text.strip() for headlines in soup.find_all("h3", class_="headline-title")]


first_parts = []
second_parts = []
combined_headlines = []
bad_words = ["mirtis", 'mirties', "karas", "trauma", "stichija", 'COVID']

for headline in headlines:
    if any(bad_word in headline for bad_word in bad_words):
        headlines.remove(headline)


for headline in headlines:
    parts = headline.split(':', 1)
    if len(parts) == 2:
        first_parts.append(parts[0].strip())
        second_parts.append(parts[1].strip())
    else:
        pass

random.shuffle(second_parts)

for index, first_part in enumerate(first_parts):
    combined_headline = first_part + ': ' + second_parts[index]
    combined_headlines.append(combined_headline)

random_combined_headline = random.choice(combined_headlines)
print(random_combined_headline)


