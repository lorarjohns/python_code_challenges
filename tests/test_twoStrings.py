from challenges.twoStrings import twoStrings
import pytest

tests = [("hello", "world", "YES"), ("hi", "world", "NO")]


@pytest.mark.parametrize("magazine, note, expected", tests)
def test_twoStrings(magazine, note, expected, capsys):
    twoStrings(magazine, note)
    out, err = capsys.readouterr()
    assert out.strip() == expected
