# -----------------------------------------------
# P.WEB.2
# -----------------------------------------------
# • Suprogramuoti žaidimą, kuris iš tinklalapio https://quotes.toscrape.com/
#   pateiks citatas, o žaidėjui reikės atspėti jų autorių. Žaidėjui neatspėjus,
#   reikia pasufleruoti autoriaus inicialus, dar kartą neatspėjus – autoriaus
#   gimimo datą ir vietą. Jeigu žaidėjas neatspėja iš 3 kartų, jam
#   atspausdinamas teisingas atsakymas ir paklausiama, ar jis nori tęsti
#   žaidimą.
# -----------------------
# English description will be added.
# -----------------------------------------------

from bs4 import BeautifulSoup
import requests
import random

author_info = []
initials = []

source = requests.get('https://quotes.toscrape.com/').text
soup = BeautifulSoup(source, 'html.parser')
quotes = [quotes.text.strip() for quotes in soup.find_all("span", class_="text")]
authors = [authors.text.strip() for authors in soup.find_all("small", class_="author")]

for author in authors:
    author_list = author.split(' ')
    author_initial = ''
    for name in author_list:
        if '.' not in name:
            author_initial += name[0] + '.'
        else:
            author_initial += name
    #author_initial = f'{author_list[0][0]}. {author_list[-1][0]}.'
    initials.append(author_initial)

random_index = random.randint(0, len(quotes) - 1)
quote = quotes[random_index]
author_name = authors[random_index]


# def keep_first_letters(input_string):
#     words = input_string.split()
#     first_letters = [word[0] for word in words]
#     result = ''.join(first_letters)
#     return result


while True:
    print(f"Whose quote is this: {quote}")
    answer = input('Your answer: ').strip()
    if answer.lower() == author_name.lower():
        print('Correct!')
        break
    else:
        print('False!')
        print(f"Your first hint is the author's initials: {initials[random_index]}")
        answer = input('Your answer: ').strip()
        if answer.lower() == author_name.lower():
            print('Correct!')
            break
        else:
            print(f"Wrong! Correct answer is {authors[random_index]}")
    if_continue = input('Continue? y/n: ')
    if if_continue != 'y':
        break
