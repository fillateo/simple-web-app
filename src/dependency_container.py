from dependency_injector import containers, providers

from src.infrastructure.repositories.email_repository import EmailRepository
from src.services.email_service import EmailService


def setup_dependency_container(app, modules=None, packages=None):
    container = DependencyContainer()
    app.container = container
    app.container.wire(modules=modules, packages=packages)
    return app


class DependencyContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration()

    email_repository = providers.Singleton(EmailRepository)

    email_service = providers.Factory(
        EmailService,
        repository=email_repository,
    )
