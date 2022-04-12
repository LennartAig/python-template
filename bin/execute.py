from example_package.example_class import ExampleClass

if __name__ == "__main__":
    obj1 = ExampleClass("Lennart", 28)
    print(obj1)
    obj2 = ExampleClass.from_string("Lennart", 1993)
    print(obj1)
    print(obj2.calculate_current_age(1993))