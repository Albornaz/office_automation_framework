import smtplib
from email.message import EmailMessage
from oaf.config import SMTP_SERVER, DEFAULT_SENDER

def send_email(to, subject, body):
    msg = EmailMessage()
    msg["From"] = DEFAULT_SENDER
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP(SMTP_SERVER) as server:
        server.send_message(msg)
