from flask import Flask

from ioc.container import DependencyContainer
from ioc.provider import DependencyProvider
from ioc.stubs import ServiceStub
from service import Service


def __register_routes(
        *,
        application: Flask,
        dependency_provider: DependencyProvider,
) -> None:
    application.add_url_rule(
        rule='/greet/',
        view_func=dependency_provider.provide_route_greet,
        methods=['GET'],
    )


def get_application() -> Flask:
    application = Flask(__name__)
    dependency_container = DependencyContainer()
    dependency_container.bind_multiple({
        ServiceStub: Service,
    })
    dependency_provider = DependencyProvider(dependency_container)
    __register_routes(
        application=application,
        dependency_provider=dependency_provider,
    )
    return application


if __name__ == '__main__':
    app = get_application()
    app.run()
