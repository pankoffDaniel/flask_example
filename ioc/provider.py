from controllers import greet
from ioc.container import DependencyContainer
from ioc.stubs import ServiceStub
from service import Service


class DependencyProvider:

    def __init__(self, container: DependencyContainer) -> None:
        self.__container = container

    def provide_service(self) -> Service:
        return self.__container.get(ServiceStub)()

    def provide_route_greet(self) -> str:
        return greet(
            service=self.provide_service(),
        )
