from example_package.example_class import ExampleClass

if __name__ == "__main__":
    obj1 = ExampleClass("Lennart", 28)
    obj2 = ExampleClass.from_string("Lennart", 1993)

    obj3 = ExampleClass.init_ones("Lennart", 29)

    try:
        obj4 = ExampleClass.init_ones("Lennart", 30)
    except AssertionError:
        print("Failed correctly as Exampled Class can only be initialized ones with init_ones")