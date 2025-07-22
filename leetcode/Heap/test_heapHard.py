from heapHard import HardSolution, FindMedianFromDataStream295
import pytest



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


