from typing import Iterator


class ExampleIterator:
    """Example for custom iterator class
    """
    def __init__(self, max: int = 0):
        self.max = max
        
    def __iter__(self) -> Iterator:
        """The __iter__() method returns the iterator object itself.
        If required, some initialization can be performed.

        Returns:
            _type_: _description_
        """
        self.n = 0
        return self
    
    def __next__(self):
        """The __next__() method must return the next item in the sequence.
        On reaching the end, and in subsequent calls, it must raise StopIteration.

        Raises:
            StopIteration: _description_

        Returns:
            _type_: _description_
        """
        if self.n <= self.max:
            result = 2**self.n
            # This is necessary to store the current state
            self.n += 1
            return result
        else:
            raise StopIteration


class ExampleGeneratorDataset:
    """Example for custom generator class
    
    Python generators are a simple way of creating iterators. All the work we mentioned above are automatically handled by generators in Python.

    A generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
    """
    def __init__(self, max: int = 0):
        self.max = max
        
    def __iter__(self) -> Iterator:
        """The __iter__() method returns the iterator object itself.
        If required, some initialization can be performed.

        Returns:
            _type_: _description_
        """
        self.n = 0
        return self
    
    def __next__(self):
        """The __next__() method must return the next item in the sequence.
        On reaching the end, and in subsequent calls, it must raise StopIteration.

        Raises:
            StopIteration: _description_

        Returns:
            _type_: _description_
        """
        if self.n <= self.max:
            result = 2**self.n
            # This is necessary to store the current state
            self.n += 1
            return result
        else:
            raise StopIteration
    