from challenges.minimumSwaps import minimumSwaps
import pytest
import os

tests = [
    ([2, 3, 4, 1, 5], 3),
    ([4, 3, 1, 2], 3),
    ([1, 3, 5, 2, 4, 6, 7], 3),
    ([7, 1, 3, 2, 4, 5, 6], 5),
]


@pytest.mark.parametrize("input, expected", tests)
def test_minimumSwaps(input, expected):
    assert minimumSwaps(input) == expected
