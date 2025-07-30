import pytest
from stackEasy import EasySolution

@pytest.mark.parametrize("input_str,expected", [
    ("abbaca", "ca"),
    ("azxxzy", "ay")
])

def test_RemoveAllAdjacentDuplicatesInString1047(input_str, expected):
    e = EasySolution()
    result = e.RemoveAllAdjacentDuplicatesInString1047(input_str)
    assert result == expected