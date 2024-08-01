from abc import ABC, abstractmethod


class ProductRepositoryInterface(ABC):


    @abstractmethod
    def filter_by_user_id(self, user_id: int):
        pass
