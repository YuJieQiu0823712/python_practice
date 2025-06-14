import pytest
from twoPointerMedium import MediumSolution

@pytest.mark.parametrize("numbers, target, expected", [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2])

])

def test_twoSumIIInputArrayIsSorted167(numbers, target, expected):
    m = MediumSolution()
    result = m.twoSumIIInputArrayIsSorted167(numbers, target)
    assert result == expected

