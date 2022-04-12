from example_package.example_generator_iterator import batches
import pytest


@pytest.mark.parametrize("input_iterable, batch_size, expected",
                         [([1, 2, 3, 4, 5, 6], 1, [[1], [2], [3], [4], [5], [6]]),
                          ([1, 2, 3, 4, 5, 6], 2, [[1, 2], [3, 4], [5, 6]]),
                          ([1, 2, 3, 4, 5, 6], 4, [[1, 2, 3, 4], [5, 6]])])
def test_batches(input_iterable, batch_size, expected):
    assert list(batches(input_iterable, batch_size)) == expected