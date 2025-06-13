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
    ("araaci", 2, 4), # "araa"
    ("aa", 1, 2), # "aa"
    ("a", 1, 1), # "a"
    ("", 2, 0) # empty string
])

def test_longestSubstringWithAtMostKDistinctCharacters340(string, k, expected):
    m = MediumSolution()
    result = m.longestSubstringWithAtMostKDistinctCharacters340(string, k)
    assert result == expected


@pytest.mark.parametrize("fruits, expected", [
    ([1,2,1], 3), # [1,2,1]
    ([0,1,2,2], 3), # [0,1,2]
    ([1,2,3,2,2], 4) # [1,2,3,2]
])

def test_fruitIntoBaskets904(fruits, expected):
    m = MediumSolution()
    result = m.fruitIntoBaskets904(fruits)
    assert result == expected


@pytest.mark.parametrize("string, expected", [
    ("abcabcbb", 3), # abc
    ("bbbbb", 1), # b
    ("pwwkew", 3), # wke
    ("", 0), # empty string
    ("a", 1) # single character
])

def test_longestSubstringWithoutRepeatingCharacters3(string, expected):
    m = MediumSolution()
    result = m.longestSubstringWithoutRepeatingCharacters3(string)
    assert result == expected

@pytest.mark.parametrize("string, k, expected", [
    ("abab", 2, 4), # "aaaa" or "bbbb"
    ("aababba", 1,4) # "aaaa" or "bbbb"
])

def test_longestRepeatingCharacterReplacement424(string, k, expected):
    m = MediumSolution()
    result = m.longestRepeatingCharacterReplacement424(string, k)
    assert result == expected


@pytest.mark.parametrize("nums, k, expected", [
    ([1,1,1,0,0,0,1,1,1,1,0], 2, 6),
    ([0,0,1,1,1,0,0], 0, 3)
])

def test_maxConsecutiveOnesIII1004(nums, k, expected):
    m = MediumSolution()
    result = m.maxConsecutiveOnesIII1004(nums, k)
    assert result == expected


@pytest.mark.parametrize("string, pattern, expected", [
    ("eidbaooo", "ab", True),       # "ba" is a permutation of "ab"
    ("eidboaoo", "ab", False)      # no permutation of "ab"
])

def test_permutationInString567(string, pattern, expected):
    m = MediumSolution()
    result = m.permutationInString567(string, pattern)
    assert result == expected

@pytest.mark.parametrize("string, pattern, expected", [
    ("cbaebabacd", "abc", [0,6]), # "cba" and "bac" are permutations of "abc"
    ("abab", "ab", [0,1,2]) # "ab", "ba", and "ab" are permutations of "ab"
])  

def test_findAllAnagramsInAString438(string, pattern, expected):
    m = MediumSolution()
    result = m.findAllAnagramsInAString438(string, pattern)
    assert result == expected