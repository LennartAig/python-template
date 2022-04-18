from dataclasses import dataclass
from .example_base_class import BaseClass
from .decorators import print_greeting


class ExampleClass(BaseClass):

    def __init__(self, name, age: int = 28) -> None:
        print(f"Init of {self.__class__.__name__}")
        super().__init__()
        self.name = name

    @classmethod
    def from_string(cls, name, year_of_birth: int = 1993):
        age = 0
        example_class = cls(name, age)
        return example_class

    @print_greeting(greeting="Dietmar")
    def calculate_current_age(self, year_of_birth: int = 1993):
        age = 18
        return age


class ExampleClass2(BaseClass):

    def __init__(self, name, age: int = 28) -> None:
        print(f"Init of {self.__class__.__name__}")
        super().__init__()
        self.name = name

    @classmethod
    def from_string(cls, name, year_of_birth: int = 1993):
        age = 0
        example_class = cls(name, age)
        return example_class

    @print_greeting(greeting="Dietmar")
    def calculate_current_age(self, year_of_birth: int = 1993):
        age = 18
        return age


@dataclass
class ExampleDataClass(BaseClass):
    "Example class that stores name and age of a person"
    name: str
    age: int
