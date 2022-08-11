from services.base_service import BaseService

class ApiClient(BaseService):
    def __init__(self, username: str, password: str) -> None:
        super().__init__()
        self.username = username
        self.password = password

    def call(self) -> None:
        self.logger.debug(f'Api username: {self.username}, Api password: {self.password}')
