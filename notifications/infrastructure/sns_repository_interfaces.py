from abc import ABC, abstractmethod


class SNSRepositoryInterface(ABC):

    @abstractmethod
    def publish_message_to_subscriber(self, email: str, message: str):
        pass

    

