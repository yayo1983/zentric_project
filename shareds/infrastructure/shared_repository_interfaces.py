from abc import ABC, abstractmethod


class SharedRepositoryInterface(ABC):

    @abstractmethod
    def get_all(self) -> dict:
        pass

    @abstractmethod
    def get_by_id(self, id: int):
        pass
