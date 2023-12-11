# -----------------------------------------------
# P.MAIL.3
# -----------------------------------------------
# • Parašyti programą, kuri kas 5 sekundes tikrintų, ar veikia serveris, ir,
#   negavusi atsako, išsiųstų el. laišką su klaidos aprašymu į jūsų el. pašto
#   dėžutę. Paprastą HTTP serverį galima paleisti konsolėje su komanda
#   python -m http.server
# -----------------------
# English description will be added.
# -----------------------------------------------

import requests
from time import sleep
import smtplib
from email.message import EmailMessage
from string import Template

google_app_password = "cubgxyscokadfxzj"

def send_mail(error):
    message = '''
    Dėmesio!

    Pranešame, kad negautas atsakas iš jūsų serverio. Klaidos žinutė tokia:

    $error
    '''
    sablonas = Template(message)

    email = EmailMessage()
    email['from'] = 'Vardas Pavardė'
    email['to'] = 'tomasgiedraitis@gmail.com'
    email['subject'] = 'Email from Python'

    email.set_content(sablonas.substitute({'error': e}), 'plain')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('ptua6.real4dmin@gmail.com', google_app_password)
        smtp.send_message(email)


while True:
    try:
        res = requests.get('http://127.0.0.1:8000')
        print(res.status_code)
        sleep(5)
    except requests.ConnectionError as e:
        send_mail(e)
        break