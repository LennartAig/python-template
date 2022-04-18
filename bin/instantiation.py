from example_package.example_class import ExampleClass, ExampleClass2, ExampleDataClass

if __name__ == "__main__":
    obj1 = ExampleClass("Lennart1", 28)
    obj2 = ExampleClass.from_string("Lennart2", 1993)
    obj3 = ExampleClass.init_ones("Lennart3", 30)
    obj4 = ExampleClass2.init_ones("Lennart4", 30)
    obj5 = ExampleDataClass("Lennart5", 32)
    obj6 = ExampleDataClass.init_ones("Lennart6", 32)
