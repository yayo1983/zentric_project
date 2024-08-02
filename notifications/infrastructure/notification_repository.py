from notifications.infrastructure.models import Notification
from shareds.infrastructure.shared_repository_interfaces import (
    SharedRepositoryInterface,
)


class NotificationRepository(SharedRepositoryInterface):
    """
    Repository class for handling operations related to notifications.

    This class implements methods to interact with the `Notification` model, providing
    functionality to retrieve notifications either as a list or by a specific ID. It extends
    from `SharedRepositoryInterface` to adhere to a shared repository contract.

    Methods:
    - get_all: Retrieves all notifications from the database, including related recipient
      information.
    - get_by_id: Retrieves a specific notification by its ID.
    """

    def get_all(self):
        """
        Retrieve all notifications from the database.

        This method fetches all notification records and their related recipient information
        using `select_related` for optimized querying. In case of an error during the retrieval
        process, a `ValueError` is raised with a descriptive message.

        Returns:
            QuerySet: A Django QuerySet containing all `Notification` objects.

        Raises:
            ValueError: If an error occurs during the retrieval process.
        """
        try:
            return Notification.objects.select_related("recipient").all().order_by("id")
        except Exception as e:
            raise ValueError(
                f"An error occurred while retrieving notifications: {e}"
            ) from e

    def get_by_id(self, notification_id: int) -> Notification:
        """
        Retrieve a notification by its ID.

        This method fetches a single `Notification` record based on the provided ID. If the
        notification with the given ID does not exist or an error occurs during retrieval, a
        `ValueError` is raised with a descriptive message.

        Args:
            notification_id (int): The ID of the notification to retrieve.

        Returns:
            Notification: The `Notification` object with the specified ID.

        Raises:
            ValueError: If the notification with the given ID does not exist or an error occurs
            during retrieval.
        """
        try:
            return Notification.objects.get(id=notification_id).order_by("id")
        except Exception as e:
            raise ValueError(
                f"An error occurred while retrieving the notification: {e}"
            ) from e
