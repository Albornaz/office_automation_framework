import smtplib
from email.message import EmailMessage

class EmailSender:
    def __init__(self, config):
        self.config = config

    def send(self, to, subject, body, attachment=None):
        msg = EmailMessage()
        msg["From"] = self.config.username
        msg["To"] = to
        msg["Subject"] = subject
        msg.set_content(body)

        if attachment:
            with open(attachment, "rb") as f:
                msg.add_attachment(
                    f.read(),
                    maintype="application",
                    subtype="pdf",
                    filename=attachment
                )

        with smtplib.SMTP(self.config.smtp_server, self.config.port) as server:
            server.starttls()
            server.login(self.config.username, self.config.password)
            server.send_message(msg)
