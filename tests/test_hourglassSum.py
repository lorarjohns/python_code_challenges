from challenges.hourglassSum import hourglassSum
import pytest
import numpy as np

tests = [
    (np.array([[-9, -9, -9, 1, 1, 1],
      [0, -9, 0, 4, 3, 2],
      [-9, -9, -9, 1, 2, 3],
      [0, 0, 8, 6, 6, 0],
      [0, 0, 0, -2, 0, 0],
      [0, 0, 1, 2, 4, 0]]), 28),

      (np.array([[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 9, 2, -4, -4, 0],
       [0, 0, 0, -2, 0, 0],
       [0, 0, -1, -2, -4, 0]]), 13),

      (np.array([[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]), 19)

]

@pytest.mark.parametrize("input, expected", tests)
def test_hourglassSum(input, expected):
    assert hourglassSum(input) == expected
