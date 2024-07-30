from notifications.infrastructure.models import Notification
from notifications.infrastructure.notification_repository_interfaces import (
    NotificationRepositoryInterface,
)


class NotificationRepository(NotificationRepositoryInterface):

    def get_all(self) -> dict:
        try:
            notifications = Notification.objects.all()
            notifications_list = list(notifications.values())
            return notifications_list
        except Exception as e:
            raise ValueError(f"An error occurred while retrieving products: {e}") from e

    def get_by_id(self, notification_id) -> Notification:
        try:
            return Notification.objects.get(id=notification_id)
        except Exception as e:
            raise ValueError(
                f"An error occurred while retrieving an notification: {e}"
            ) from e
