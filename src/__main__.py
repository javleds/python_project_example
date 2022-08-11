from dependency_injector.wiring import Provide, inject

from services.api_client import ApiClient
from containers import Container

@inject
def main(api_service: ApiClient = Provide[Container.api_client]) -> None:
    api_service.call()

if __name__ == '__main__':
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    main()