import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

name = 'Yumi'
html = Template(Path('email_send.html').read_text())
email = EmailMessage()
email['From'] = 'Your Name'
email['To'] = 'user_email@gmail.com'
email['Subject'] = f'It\'s your lucky day {name}'
email.set_content(html.substitute({'name': name}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your_email@gmail.com', 'your_password')
    smtp.send_message(email)
    print('message sent')