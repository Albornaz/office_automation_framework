import smtplib
from email.message import EmailMessage
from pathlib import Path
from oaf.config import SMTP_SERVER, DEFAULT_SENDER

def send_email_with_attachment(
    to: str,
    subject: str,
    body: str,
    attachment_path: str
):
    msg = EmailMessage()
    msg["From"] = DEFAULT_SENDER
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    path = Path(attachment_path)
    with open(path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=path.name
        )

    with smtplib.SMTP(SMTP_SERVER) as server:
        server.send_message(msg)

    print(f"Email sent to {to} with attachment.")

