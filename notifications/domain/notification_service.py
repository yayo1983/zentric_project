from notifications.infrastructure.notification_repository_interfaces import (
    NotificationRepositoryInterface,
)
from notifications.infrastructure.models import Notification


class NotificationService:
    def __init__(self, notification_repository: NotificationRepositoryInterface):
        self.notification_repository = notification_repository

    def get_all(self) -> dict:
        try:
            return self.notification_repository.get_all()
        except Exception as e:
            raise

    def get_by_id(self, product_id) -> Notification:
        try:
            return self.notification_repository.get_by_id(product_id)
        except Exception as e:
            raise
