# -----------------------------------------------
# P.MAIL.2
# -----------------------------------------------
# • Parašyti funkciją, kuri kaip argumentus priimtų kreipinį, el. pašto adresą
#   ir skolą (float tipo reikšmę), ir sugeneruotų laišką, kuriame informuotų
#   adresatą apie susidariusį įsiskolinimą. Laiške kur nors turėtų būti
#   įterptas logotipas.
# -----------------------
# English description will be added.
# -----------------------------------------------

import smtplib
from email.message import EmailMessage
from string import Template

google_app_password = "cubgxyscokadfxzj"


def apmokek(kreipinys, elpastas, suma):
    with open('skola.html', 'r', encoding='utf-8') as f:
        html = f.read()

    sablonas = Template(html)

    email = EmailMessage()
    email['from'] = 'Skolos administratorius'
    email['to'] = elpastas
    email['subject'] = 'Pranešimas apie įsiskolinimą'

    email.set_content(sablonas.substitute(
        {'kreipinys': kreipinys,
         'skola': suma,
         'mail': elpastas}),
        'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('ptua6.real4dmin@gmail.com', google_app_password)
        smtp.send_message(email)


apmokek('Silvestrai', 'ramanauskienesilvija@gmail.com', 25.25)

