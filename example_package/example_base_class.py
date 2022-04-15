from abc import ABC


class BaseClass(ABC):
    __number_of_instances: int = 0
    __initialized: bool = False

    def __init__(self) -> None:
        super().__init__()
        print("Init of BaseClass")
        self.__number_of_instances = self.__number_of_instances + 1
        self.__initialized = True

    # For call to repr(). Prints object's information
    @classmethod
    def __repr__(self):
        return f"Current Number of instances of class {self.__name__}: {self.__number_of_instances}"

    @classmethod
    def init_ones(cls, *args, **kwargs):
        if cls.__initialized:
            print(f"{cls.__name__} is already initialized")
            raise AssertionError
        else:
            cls.__initialized = True
            return cls(args, kwargs)
