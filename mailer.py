import os

import yagmail


def send_mail(text, subject, recipient):
    username = os.getenv("GMAIL_USERNAME")
    password = os.getenv("GMAIL_PASSWORD")
    yagmail.SMTP(username, password).send(recipient, subject, text)
