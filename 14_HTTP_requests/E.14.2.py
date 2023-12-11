# -----------------------------------------------
# P.REQ.2
# -----------------------------------------------
# • Parašyti funkciją, kuri kaip argumentus priimtų tinklalapių URL eilučių
#   sąrašą ir grąžintų, kokį serverį naudoja kiekvienas tinklalapis. Atsakymas
#   galėtų atrodyti maždaug taip:
#     =========================================================================
#     URL                     Server
#     -------------------------------------
#     https://www.delfi.lt/   DWS
#     https://www.alfa.lt/    nginx/1.10.3 (Ubuntu)
#     https://www.15min.lt/   nginx
#     https://www.lrytas.lt/  shield
#     http://www.google.com/  gws
#     =========================================================================
# -----------------------
# English description will be added.
# -----------------------------------------------

import requests

urls = ['https://peps.python.org/pep-0008/', 'https://www.google.com', 'https://www.quantus.lt/', 'https://edition.cnn.com/']


def get_server_info(url_list):
    for url in url_list:
        response = requests.head(url)
        server = response.headers.get('Server')
        print(f"{url} {server}")


get_server_info(urls)

