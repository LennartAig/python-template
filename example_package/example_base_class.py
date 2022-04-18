from abc import ABC


class BaseClass(ABC):
    __number_of_instances: int = 0
    __initialized: bool = False
    __instance: object

    def __new__(cls, *args, **kwargs):
        print(f"Create a new instance of class {cls.__name__}.")
        cls.__number_of_instances += 1
        cls.__initialized = True
        cls.__instance = super().__new__(cls)
        cls.__instance.__init__(*args, **kwargs)
        return super().__new__(cls)

    # For call to repr(). Prints object's information
    @classmethod
    def __repr__(cls):
        return f"Current Number of instances of class {cls.__name__} with name: {cls.__number_of_instances}"

    @classmethod
    def init_ones(cls, *args, **kwargs):
        if cls.__initialized:
            print(f"{cls.__name__} is already initialized")
            return cls.__instance
        else:
            print(f"{cls.__name__} gets initialized")
            cls.__initialized = True
            return cls(args, kwargs)
