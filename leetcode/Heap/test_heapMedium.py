from heapMedium import MediumSolution
import pytest

@pytest.mark.parametrize("nums, k, expected", [
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)
])

def test_kthLargestElementInAnArray215(nums, k, expected):
    m = MediumSolution()
    result = m.kthLargestElementInAnArray215(nums, k)
    assert result == expected