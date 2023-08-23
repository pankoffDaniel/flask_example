from service import Service


def greet(*, service: Service) -> str:
    result = service.do_something()
    return result
