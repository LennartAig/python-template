from abc import ABC


class BaseClass(ABC):
    __number_of_instances: int = 0

    def __init__(self) -> None:
        super().__init__()
        print("Init of BaseClass")
        self.__number_of_instances += 1

    # For call to repr(). Prints object's information
    @classmethod
    def __repr__(self):
        return f"Current Number of instances of class {self.__name__}: {self.__number_of_instances}"
