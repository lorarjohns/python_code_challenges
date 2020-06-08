from challenges.minimumBribes import minimumBribes
import pytest
import os

tests = [([2, 1, 5, 3, 4], 3),
         ([2, 5, 1, 3, 4], 'Too chaotic'),
         ([5, 1, 2, 3, 7, 8, 6, 4], 'Too chaotic'),
         ([1, 2, 5, 3, 7, 8, 6, 4], 7),
         ([1, 2, 5, 3, 4, 7, 8, 6], 4)]

@pytest.mark.parametrize("input, expected", tests)
def test_hourglassSum(input, expected):
    assert minimumBribes(input) == expected
