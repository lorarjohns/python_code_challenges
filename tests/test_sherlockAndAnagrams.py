from challenges.sherlockAndAnagrams import sherlockAndAnagrams
import pytest

tests = [

    ("ifailuhkqq", 3),
    ("kkkk", 10),
    ("abba", 4),
    ("abcd", 0)
]

@pytest.mark.parametrize("input, expected", tests)
def test_sherlockAndAnagrams(input, expected):
    assert sherlockAndAnagrams(input) == expected