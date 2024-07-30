from abc import ABC, abstractmethod
from shareds.infrastructure.shared_repository_interfaces import SharedRepositoryInterface
from shareds.domain.abstract_service import AbstractService
from shareds.application.abstract_serializer import AbstractSerializer


class AbstractFactory(ABC):
    @abstractmethod
    def create_service(self, shared_repository: SharedRepositoryInterface) -> AbstractService:
        pass

    @abstractmethod
    def create_serializer(self) -> AbstractSerializer:
        pass
    
    @abstractmethod
    def create_repository(self):
        pass