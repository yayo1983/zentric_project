from shareds.domain.sns_service import SNService
from shareds.abstract_sns_factory import AbstractSNSFactory
from shareds.infrastructure.sns_repository_adapter import SNSRepositoryAdapter


class SNSFactory(AbstractSNSFactory):

    def create_service(
        self, sns_repository: SNSRepositoryAdapter) -> SNService:
        return SNService(sns_repository)
        
    def create_repository(self) -> SNSRepositoryAdapter:
        return SNSRepositoryAdapter()

