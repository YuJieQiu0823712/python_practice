import pytest
from slidingWindowMedium import MediumSolution

@pytest.mark.parametrize("target, nums, expected", [
    (7, [2,3,1,2,4,3], 2),
    (4, [1,4,4], 1),
    (11, [1,1,1,1,1,1,1], 0)
])

def test_minSubArrayLen209(target, nums, expected):
    m = MediumSolution()
    result = m.minSubArrayLen209(target, nums)
    assert result == expected

@pytest.mark.parametrize("string, k, expected", [
    ("araaci", 2, 4),
    ("aa", 1, 2),
    ("a", 1, 1),
    ("", 2, 0)
])

def test_longestSubstringWithAtMostKDistinctCharacters340(string, k, expected):
    m = MediumSolution()
    result = m.longestSubstringWithAtMostKDistinctCharacters340(string, k)
    assert result == expected