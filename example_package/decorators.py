def print_hello_world(func):

    def wrapper(*args, **kwargs):
        print("Hello world")
        return func(*args, **kwargs)

    return wrapper