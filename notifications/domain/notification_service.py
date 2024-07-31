from shareds.infrastructure.shared_repository_interfaces import (
    SharedRepositoryInterface,
)
from notifications.infrastructure.models import Notification
from shareds.domain.abstract_service import AbstractService


class NotificationService(AbstractService):
    def __init__(self, notification_repository: SharedRepositoryInterface):
        self.notification_repository = notification_repository

    def get_all(self):
        try:
            return self.notification_repository.get_all()
        except Exception as e:
            raise

    def get_by_id(self, notification_id) -> Notification:
        try:
            return self.notification_repository.get_by_id(notification_id)
        except Exception as e:
            raise
