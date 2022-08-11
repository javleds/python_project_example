import logging.config

from dependency_injector import containers, providers

from services.api_client import ApiClient

class Container(containers.DeclarativeContainer):
    config = providers.Configuration(ini_files=['config.ini'])

    logging = providers.Resource(
        logging.config.fileConfig,
        fname='logging.ini',
    )

    api_client = providers.Singleton(
        ApiClient,
        username=config.api_keys.username,
        password=config.api_keys.password,
    )