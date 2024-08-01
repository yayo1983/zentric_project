from shareds.infrastructure.shared_repository_interfaces import (
    SharedRepositoryInterface,
)
from notifications.infrastructure.models import Notification
from notifications.infrastructure.sns_repository_interfaces import (
    SNSRepositoryInterface,
)
from shareds.domain.abstract_service import AbstractService
from notifications.domain.abstract_sns_service import AbstractSNSService

class NotificationService(AbstractService, AbstractSNSService):
    def __init__(
        self,
        notification_repository: SharedRepositoryInterface,
        sns_repository: SNSRepositoryInterface,
    ):
        self.notification_repository = notification_repository
        self.sns_repository = sns_repository

    def get_all(self):
        try:
            return self.notification_repository.get_all()
        except Exception as e:
            raise

    def get_by_id(self, notification_id: int) -> Notification:
        try:
            return self.notification_repository.get_by_id(notification_id)
        except Exception as e:
            raise

    def publish_message_to_subscriber(self, email: str, message: str):
        return self.sns_repository.publish_message_to_subscriber(email, message)
