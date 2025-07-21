from heapMedium import MediumSolution, FindMedianFromDataStream295
import pytest

@pytest.mark.parametrize("nums, k, expected", [
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)
])

def test_kthLargestElementInAnArray215(nums, k, expected):
    m = MediumSolution()
    result = m.kthLargestElementInAnArray215(nums, k)
    assert result == expected


@pytest.mark.parametrize("tasks, n, expected", [
    (["A","A","A","B","B","B"], 2, 8), # A -> B -> idle -> A -> B -> idle -> A -> B
    (["A","A","A","B","B","B"], 0, 6), # A -> A -> A -> B -> B -> B
])

def test_taskScheduler621(tasks, n, expected):
    m = MediumSolution()
    result = m.taskScheduler621(tasks, n)
    assert result == expected


@pytest.mark.parametrize("sequence, expected_medians", [
    ([1, 2, 3], [1.0, 1.5, 2.0]),
    ([5, 15, 1, 3], [5.0, 10.0, 5.0, 4.0])
])

def test_FindMedianFromDataStream295(sequence, expected_medians):
    median_finder = FindMedianFromDataStream295()
    result = []
    for num in sequence:
        median_finder.addNum(num)
        result.append(median_finder.findMedian())
    assert result == expected_medians


