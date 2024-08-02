from shareds.infrastructure.sns_repository_interfaces import (
    SNSRepositoryInterface,
)
from shareds.domain.abstract_sns_service import AbstractSNSService


class SNService(AbstractSNSService):
    def __init__(
        self,
        sns_repository: SNSRepositoryInterface
    ):
        self.sns_repository = sns_repository


    def publish_message_to_subscriber(self, email: str, message: str):
        return self.sns_repository.publish_message_to_subscriber(email, message)

   