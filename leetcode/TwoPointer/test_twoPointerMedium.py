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


@pytest.mark.parametrize("nums, expected", [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]])
])

def test_threeSum15(nums, expected):
    m = MediumSolution()
    result = m.threeSum15(nums)
    # Sort inner lists and outer list for comparison
    assert sorted([sorted(triplet) for triplet in result]) == sorted([sorted(triplet) for triplet in expected])


@pytest.mark.parametrize("nums, target, expected", [
    ([-1,2,1,-4], 1, 2), # The closest sum is -1 + 2 + 1 = 2
    ([0,0,0], 1, 0) # The closest sum is 0 + 0 + 0 = 0
])

def test_threeSumClosest16(nums, target, expected):
    m = MediumSolution()
    result = m.threeSumClosest16(nums, target)
    assert result == expected


@pytest.mark.parametrize("nums, target, expected", [
     ([-2, 0, 1, 3], 2, 2) # [-2,0,1] and [-2,0,3]
])

def test_threeSumSmaller259(nums, target, expected):
    m = MediumSolution()
    result = m.threeSumSmaller259(nums, target)
    assert result == expected


@pytest.mark.parametrize("nums, target, expected", [
    ([10, 5, 2, 6], 100, 8)
    # [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]   
])

def test_SubarrayProductLessThanK713(nums, target, expected):
    m = MediumSolution()
    result = m.SubarrayProductLessThanK713(nums, target)
    assert result == expected


@pytest.mark.parametrize("input_list,expected", [
    ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2])
])

def test_sortNumbers75(input_list, expected):
    m = MediumSolution()
    result = m.sortNumbers75(input_list)
    assert result == expected


@pytest.mark.parametrize("nums, target, expected", [
    ([1, 0, -1, 0, -2, 2], 0, sorted([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])),
    ([], 0, []) # Empty list

])

def test_fourSum18(nums, target, expected):
    m = MediumSolution()
    result = m.fourSum18(nums, target)
    assert sorted(result) == sorted(expected)