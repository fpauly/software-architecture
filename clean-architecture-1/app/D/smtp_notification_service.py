import smtplib
from email.message import EmailMessage
from ..B.notification_service import NotificationService

class SMTPNotificationService(NotificationService):

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to: str, subject: str, body: str) -> None:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = self.username
        msg["To"] = to
        msg.set_content(body)

        #with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
        #    server.login(self.username, self.password)
        #    server.send_message(msg)

        print(f"Simulating email delivery to {to}")
        print(f"Subject: {subject}")
        print(f"Message: {body}")
        print("=" * 50)
