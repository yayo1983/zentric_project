from abc import ABC, abstractmethod

class AbstractService(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id: int):
        pass
