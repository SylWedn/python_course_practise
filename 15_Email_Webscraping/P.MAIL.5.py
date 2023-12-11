import smtplib
from email.message import EmailMessage
from string import Template
google_app_password = "cubgxyscokadfxzj"


def apmokek(kreipinys, elpastas, suma):
    with open('skola2.html', 'r', encoding='utf-8') as f:
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

    with open('elephant.png', 'rb') as file:
        content = file.read()
        email.add_attachment(
            content,
            maintype='image/png',
            subtype='png',
            filename='elephant.png')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('ptua6.real4dmin@gmail.com', google_app_password)
        smtp.send_message(email)


apmokek('Silvestrai', 'silvonmc@gmail.com', 25.25)
