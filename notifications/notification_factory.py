from notifications.domain.notification_service import NotificationService
from notifications.application.serializers import NotificationSerializer
from shareds.infrastructure.shared_repository_interfaces import (
    SharedRepositoryInterface,
)
from notifications.infrastructure.notification_repository import NotificationRepository
from shareds.infrastructure.sns_repository_adapter import SNSRepositoryAdapter
from shareds.abstract_factory import AbstractFactory


class NotificationFactory(AbstractFactory):

    def create_service(
        self, shared_repository: SharedRepositoryInterface
    ) -> NotificationService:

        return NotificationService(shared_repository, self.create_sns_repository())

    def create_serializer(self) -> NotificationSerializer:
        return NotificationSerializer()

    def create_repository(self) -> NotificationRepository:
        return NotificationRepository()

    def create_sns_repository(self) -> SNSRepositoryAdapter:
        return SNSRepositoryAdapter()
