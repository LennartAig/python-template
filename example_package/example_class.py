from .example_base_class import BaseClass
from .decorators import print_hello_world


class ExampleClass(BaseClass):

    def __init__(self, name, age: int = 28) -> None:
        super().__init__()
        self.name = name

    @classmethod
    def from_string(cls, name, year_of_birth: int = 1993):
        age = 0
        example_class = cls(name, age)
        return example_class

    @print_hello_world
    def calculate_current_age(self, year_of_birth: int = 1993):
        age = 18
        return age
