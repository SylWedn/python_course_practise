
# • Tinklapis https://cataas.com/cat kas kartą užkrauna vis skirtingą katės
#   nuotrauką. Parašykite funkciją, kuriai kaip argumentą pateikus, kiek norime
#   nuotraukų, išsaugotų jas jūsų kompiuteryje.

import requests


def download_cat_picture(num_photos):
    for i in range(num_photos):
        r = requests.get('https://cataas.com/cat')
        filename = f'cat_{i+1}'
        with open(f'{filename}.png', 'wb') as f:
            f.write(r.content)

download_cat_picture(5)

