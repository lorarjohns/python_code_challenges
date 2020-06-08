from challenges.hourglassSum import hourglassSum, read_from_file
import pytest
import os

inputs = [read_from_file(os.path.join('tests/2d-array-testcases/input', fp)) for fp in os.listdir("tests/2d-array-testcases/input")]
outputs = [read_from_file(os.path.join('tests/2d-array-testcases/output', fp)) for fp in os.listdir("tests/2d-array-testcases/output")]

assert len(inputs) == len(outputs)

tests = list(zip(inputs, outputs))
print(tests)

@pytest.mark.parametrize("input, expected", tests)
def test_hourglassSum(input, expected):
    assert hourglassSum(input) == expected
