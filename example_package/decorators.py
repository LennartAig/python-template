from typing import Optional, Callable


def print_hello_world(func):

    def wrapper(*args, **kwargs):
        print("Hello world")
        return func(*args, **kwargs)

    return wrapper


def print_greeting(greeting: Optional[str] = "World"):

    def inner_decorator(func):

        def wrapper(*args, **kwargs):
            print(f"Hello {greeting}")
            return func(*args, **kwargs)

        return wrapper

    return inner_decorator