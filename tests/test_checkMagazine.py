from challenges.checkMagazine import checkMagazine
import pytest

tests = [
    
    ("ive got a lovely bunch of coconuts".split(), "ive got some coconuts".split(), "No"),
    ("two times three is not four".split(), "two times two is four".split(), "No"),
    ("give me one grand today night".split(), "give me one grand today".split(), "Yes")
]

@pytest.mark.parametrize("magazine, note, expected", tests)
def test_checkMagazine(magazine, note, expected, capsys):
    checkMagazine(magazine, note)
    out, err = capsys.readouterr()
    assert out.strip() == expected