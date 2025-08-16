import pytest
from subsetsMedium import mediumSolution

@pytest.mark.parametrize("nums, expected", [
        ([1], [[], [1]]),  
        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]) 
])
def test_subsets78(nums, expected):
    m = mediumSolution()
    result = m.subsets78(nums)
    assert result == expected

    
@pytest.mark.parametrize("nums, expected", [
        ([1, 2, 2], [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]),
        ([0], [[], [0]])
])
def test_subsetsWithDup90(nums, expected):
    m = mediumSolution()
    result = m.subsetsWithDup90(nums)
    assert result == expected


@pytest.mark.parametrize("input_str,expected", [
        ("a1b2", ["a1b2", "A1b2", "a1B2", "A1B2"]),
        ("3z4", ["3z4", "3Z4"])
])
def test_letterCasePermutation784(input_str, expected):
    m = mediumSolution()
    result = m.letterCasePermutation784(input_str)
    assert result == expected

@pytest.mark.parametrize("n, expected", [
        (3, ["((()))","(()())","(())()","()(())","()()()"]),
        (1, ["()"])
])
def test_generateParentheses22(n, expected):
    m = mediumSolution()
    result = m.generateParentheses22(n)
    assert sorted(result) == sorted(expected)