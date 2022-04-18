from typing import Iterable, Iterator, List, Any


class ExampleIterator(object):
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


def batches(iterable: Iterable[Any], batch_size: int) -> Iterable[List[Any]]:
    batch = []
    for item in iterable:
        batch.append(item)

        if len(batch) == batch_size:
            yield batch
            batch = []
    # output rest if not fit into batchsize
    if batch:
        yield batch
