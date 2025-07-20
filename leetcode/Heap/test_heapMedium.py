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


@pytest.mark.parametrize("tasks, n, expected", [
    (["A","A","A","B","B","B"], 2, 8), # A -> B -> idle -> A -> B -> idle -> A -> B
    (["A","A","A","B","B","B"], 0, 6), # A -> A -> A -> B -> B -> B
])

def test_taskScheduler621(tasks, n, expected):
    m = MediumSolution()
    result = m.taskScheduler621(tasks, n)
    assert result == expected