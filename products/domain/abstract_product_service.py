from abc import ABC, abstractmethod

class AbstractProductService(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def filter_by_user_id(self, user_id: int):
        pass
