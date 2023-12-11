# -----------------------------------------------
# P.WEB.2
# -----------------------------------------------
# • Suprogramuoti žaidimą, kuris iš tinklapio https://quotes.toscrape.com/
#   pateiks citatas, o žaidėjui reikės atspėti jų autorių. Žaidėjui neatspėjus,
#   reikia pasufleruoti autoriaus inicialus, dar kartą neatspėjus – autoriaus
#   gimimo datą ir vietą. Jeigu žaidėjas neatspėja iš 3 kartų, jam
#   atspausdinamas teisingas atsakymas ir paklausiama, ar jis nori tęsti
#   žaidimą.
# -----------------------
# English description will be added.
# -----------------------------------------------
# -----------------------------------------------
# P.WEB.2
# -----------------------------------------------
# • Suprogramuoti žaidimą, kuris iš tinklapio https://quotes.toscrape.com/
#   pateiks citatas, o žaidėjui reikės atspėti jų autorių. Žaidėjui neatspėjus,
#   reikia pasufleruoti autoriaus inicialus, dar kartą neatspėjus – autoriaus
#   gimimo datą ir vietą. Jeigu žaidėjas neatspėja iš 3 kartų, jam
#   atspausdinamas teisingas atsakymas ir paklausiama, ar jis nori tęsti
#   žaidimą.
# -----------------------
# English description will be added.
# -----------------------------------------------

from random import randint

import requests
from bs4 import BeautifulSoup

html = requests.get('https://quotes.toscrape.com').text
soup = BeautifulSoup(html, "html.parser")

# quotes
quote_tags = soup.select('.text')
quotes = [quote.get_text() for quote in quote_tags]

# urls
all_url_tags = soup.find_all('a', attrs={'class': None})
url_tags = [url_tag for url_tag in all_url_tags if url_tag.get_text() == "(about)"]
relative_urls = [url_tag['href'] for url_tag in url_tags]

# answers
author_tags = soup.find_all('small', class_='author')
answers = [answer.get_text() for answer in author_tags]

# frst hints
first_hints = []
for answer in answers:
    answer_split = answer.split()
    first_hint = ''
    for name in answer_split:
        if '.' not in name:
            first_hint += f"{name[0]}."
        else:
            first_hint += name
    first_hints.append(first_hint)

# second hints
second_hints = []
for relative_url in relative_urls:
    html_for_second_hint = requests.get('https://quotes.toscrape.com' + relative_url).text
    soup = BeautifulSoup(html_for_second_hint, "html.parser")
    p_tags = soup.select('p')
    needed_p_tag = p_tags[1]
    second_hint = needed_p_tag.get_text()
    second_hints.append(second_hint)

# main game loop
while True:
    i = randint(0, 9)
    print('\n', quotes[i])
    answer1 = input('Your answer: ')
    if answer1 == answers[i]:
        print(f"Correct! Answer is {answers[i]}")
    else:
        print(first_hints[i])
        answer2 = input('Your answer: ')
        if answer2 == answers[i]:
            print(f"Correct! Answer is {answers[i]}")
        else:
            print(second_hints[i])
            answer3 = input('Your answer: ')
            if answer3 == answers[i]:
                print(f"Correct! Answer is {answers[i]}")
            else:
                print(f"Wrong! Correct answer is {answers[i]}")
    if_continue = input('Continue? y/n: ')
    if if_continue != 'y':
        break