from challenges.arrayManipulation import arrayManipulation
import pytest
import os

tests = [
    (10, [(1, 5, 3), (4, 8, 7), (6, 9, 1)], 10),
    (5, [(1, 2, 100), (2, 5, 100), (3, 4, 100)], 200),
]


@pytest.mark.parametrize("n, queries, expected", tests)
def test_arrayManipulation(n, queries, expected):
    assert arrayManipulation(n, queries) == expected
