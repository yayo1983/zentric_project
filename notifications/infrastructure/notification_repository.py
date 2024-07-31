from notifications.infrastructure.models import Notification
from shareds.infrastructure.shared_repository_interfaces import (
    SharedRepositoryInterface,
)


class NotificationRepository(SharedRepositoryInterface):

    def get_all(self):
        try:
            return Notification.objects.select_related('recipient').all()
        except Exception as e:
            raise ValueError(f"An error occurred while retrieving products: {e}") from e

    def get_by_id(self, notification_id: int) -> Notification:
        try:
            return Notification.objects.get(id=notification_id)
        except Exception as e:
            raise ValueError(
                f"An error occurred while retrieving an notification: {e}"
            ) from e
