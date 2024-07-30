from abc import ABC, abstractmethod
from notifications.infrastructure.models import Notification

class NotificationRepositoryInterface(ABC):
    
    @abstractmethod
    def get_all(self) -> dict:
        pass
    
    @abstractmethod
    def get_by_id(self, product_id) -> Notification:
        pass