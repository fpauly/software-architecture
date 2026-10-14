from .notification_service import NotificationService
from ..entities.user import User

def notify_user(notification_service: NotificationService, user: User):
    subject = "Welcome!"
    body = user.welcome_message()
    notification_service.send_email(user.email, subject, body)

