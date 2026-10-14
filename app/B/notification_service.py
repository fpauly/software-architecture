from abc import ABC, abstractmethod

class NotificationService(ABC):
    """Abstract base class for notification services."""
    
    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> None:
        pass
