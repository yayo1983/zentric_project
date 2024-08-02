from abc import ABC, abstractmethod
from shareds.infrastructure.sns_repository_adapter import SNSRepositoryAdapter
from shareds.domain.abstract_sns_service import AbstractSNSService
from shareds.infrastructure.sns_repository_interfaces import SNSRepositoryInterface

class AbstractSNSFactory(ABC):
    @abstractmethod
    def create_service(self, sns_repository: SNSRepositoryAdapter) -> AbstractSNSService:
        pass
    
    @abstractmethod
    def create_repository(self) -> SNSRepositoryInterface:
        pass
