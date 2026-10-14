from app.D.smtp_notification_service import SMTPNotificationService
from app.C.user import User
from app.B.notify_user import notify_user

def main():

    smtp_service = SMTPNotificationService(
        smtp_server="smtp.nonexistent.turkuamk.fi",
        smtp_port=465,
        username="tuomo.helo@turkuamk.fi",
        password="your_password"
    )

    target_user = User(email="targetuser@example.com", name="Target User")

    notify_user(smtp_service, target_user)

if __name__ == "__main__":
    main()
