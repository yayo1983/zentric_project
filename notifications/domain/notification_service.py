from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from shareds.infrastructure.shared_repository_interfaces import (
    SharedRepositoryInterface,
)
from notifications.infrastructure.models import Notification
from shareds.domain.abstract_service import AbstractService


class NotificationService(AbstractService):
    def __init__(
        self,
        notification_repository: SharedRepositoryInterface
    ):
        self.notification_repository = notification_repository

    def get_all(self):
        return self.notification_repository.get_all()

    def get_by_id(self, id: int) -> Notification:
        return self.notification_repository.get_by_id(id)

    def get_email_user(self, user_id: int) -> str:
        """_summary_
            Send message to subscriber
        Args:
            user_id (int): id of user selected to notifications

        Raises:
            ValueError: if no exist the email
            ValueError: Appear an unexpected error

        Returns:
            str: return the email
        """        
        try:
            user = User.objects.get(id=user_id)
            return user.email
        except ObjectDoesNotExist:
            raise ValueError(f"No user found with ID {user_id}.") from None
        except Exception as e:
            raise ValueError(f"An unexpected error occurred while retrieving the user: {e}") from e
