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