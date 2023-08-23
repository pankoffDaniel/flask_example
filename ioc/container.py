from typing import Callable, Any


class DependencyContainer:

    def __init__(self) -> None:
        self.__bindings: dict[Callable, Callable] = {}

    def bind(self, interface: Callable, implementation: Callable) -> None:
        self.__bindings[interface] = implementation

    def bind_multiple(self, bindings: dict) -> None:
        for interface, implementation in bindings.items():
            self.bind(interface, implementation)

    def get(self, interface: Callable) -> Any:
        return self.__bindings[interface]
