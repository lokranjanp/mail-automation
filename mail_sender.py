import smtplib
from email.mime.text import MIMEText
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT

class EmailSender:
    def __init__(self):
        self.server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        self.server.starttls()
        self.server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    def send_email(self, to_email, subject, body):
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = EMAIL_ADDRESS
        message["To"] = to_email
        self.server.sendmail(EMAIL_ADDRESS, to_email, message.as_string())

    def close(self):
        self.server.quit()
