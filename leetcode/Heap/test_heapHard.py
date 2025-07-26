from heapHard import HardSolution, FindMedianFromDataStream295, SlidingWindowMedian480
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


@pytest.mark.parametrize("nums, k, expected", [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [1.0, -1.0, -1.0, 3.0, 5.0, 6.0])
])

def test_median_sliding_window(nums, k, expected):
    solver = SlidingWindowMedian480()
    output = solver.medianSlidingWindow(nums, k)
    assert output == pytest.approx(expected, rel=1e-9)  # Use approx to handle float comparison
    

@pytest.mark.parametrize("grid, expected", [
    (
        [
            ["#", "#", "#", "#", "#", "#"],
            ["#", "T", "#", "#", "#", "#"],
            ["#", ".", ".", "B", ".", "#"],
            ["#", ".", "#", "#", ".", "#"],
            ["#", ".", ".", ".", "S", "#"],
            ["#", "#", "#", "#", "#", "#"]
        ],
        3
    ),
    (
        [
            ["#", "#", "#", "#", "#", "#"],
            ["#", "T", "#", "#", "#", "#"],
            ["#", ".", ".", "B", ".", "#"],
            ["#", "#", "#", "#", ".", "#"],
            ["#", ".", ".", ".", "S", "#"],
            ["#", "#", "#", "#", "#", "#"]
        ],
        -1
    ),
])

def test_MinPushBox1263(grid, expected):
    h = HardSolution()
    result = h.minPushBox1263(grid)
    assert result == expected