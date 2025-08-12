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