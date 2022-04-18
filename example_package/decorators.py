from typing import Optional, Callable
from functools import wraps


def print_hello_world(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Hello world")
        return func(*args, **kwargs)

    return wrapper


def print_greeting(greeting: Optional[str] = "World"):

    def inner_decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Hello {greeting}")
            return func(*args, **kwargs)

        return wrapper

    return inner_decorator