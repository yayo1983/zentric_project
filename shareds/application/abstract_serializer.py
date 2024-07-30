from abc import ABC, abstractmethod
from rest_framework import serializers


class AbstractSerializer(ABC):
    @abstractmethod
    def get_serializer_class(self):
        pass
    
class CommonMetaClass(type(serializers.ModelSerializer), type(AbstractSerializer)):
    pass
