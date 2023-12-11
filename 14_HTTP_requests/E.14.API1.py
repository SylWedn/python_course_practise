# -----------------------------------------------
# P.API.1
# -----------------------------------------------
# • Sukurti programą, kuri grąžina įvestos valiutų poros dabartinį kursą, tam
#   naudojant Frankfurter API adresu https://api.frankfurter.app/. API
#   dokumentacija pateikta adresu https://www.frankfurter.app/docs/. Rezultatas
#   galėtų atrodyti taip:
#     =========================================================================
#     get_rate('EUR', 'GBP')
#     # EUR-GBP:    0.84828
#
#     get_rate('ZZZ', 'GBP')
#     # Neteisingai suvestos valiutos. Galimų variantų sąrašas:
#     # ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP',
#     # 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN',
#     # 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB',
#     # 'TRY', 'USD', 'ZAR']
#     =========================================================================
# -----------------------
# English description will be added.
# -----------------------------------------------
import requests
import json

currencies = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK',
              'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR',
              'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP',
              'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD',
              'ZAR']


def get_rate(currency1, currency2):
    if currency1 not in currencies or currency2 not in currencies:
        print("Error: Neteisingai suvestos valiutos. Galimų variantų sąrašas:")
        print(currencies)
        return

    url = 'https://api.frankfurter.app/latest?amount=1&from=' + currency1 + '&to=' + currency2
    response = requests.get(url)
    data = json.loads(response.text)
    # data = {'amount': 1.0,
    #         'base': 'EUR',
    #         'date': '2023-08-03',
    #         'rates': {'GBP': 0.86468}}

    # print(currency1 + '-' + currency2 + ':    ' + str(data['rates'][currency2]))
    print(f"{currency1}-{currency2}: {data['rates'][currency2]}")


get_rate('EUR', 'GBP')

# get_rate('ZZZ', 'GBP')
