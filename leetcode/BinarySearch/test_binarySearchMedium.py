import pytest
from binarySearchMedium import TreeNode, MediumSolution

def build_tree_from_level_order(input_list):
    if not input_list:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in input_list]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def tree_to_level_order_list(root):
    from collections import deque
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)
    # Trim trailing None input_list
    while result and result[-1] is None:
        result.pop()
    return result


@pytest.mark.parametrize("nums, target, expected", [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([2, 2, 2, 2], 2, [0, 3])
])

def test_findFirstAndLastPositionOfElementInSortedArray34(nums, target, expected):
    m = MediumSolution()
    result = m.findFirstAndLastPositionOfElementInSortedArray34(nums, target)
    assert result == expected


@pytest.mark.parametrize("nums, target, expected", [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1)
])

def test_searchInRotatedSortedArray33(nums, target, expected):
    m = MediumSolution()
    result = m.searchInRotatedSortedArray33(nums, target)
    assert result == expected   


@pytest.mark.parametrize("input_list, expected", [
    ([1, None, 2, None, 3, None, 4, None, None], [2, 1, 3, None, None, None, 4])
])

def test_balanceABinarySearchTree1382(input_list, expected):
    m = MediumSolution()
    root = build_tree_from_level_order(input_list)
    balanced_root = m.balanceABinarySearchTree1382(root)
    result = tree_to_level_order_list(balanced_root)
    assert result == expected


@pytest.mark.parametrize("nums, k, expected", [
    ([4, 7, 9, 10], 1, 5),
    ([4, 7, 9, 10], 3, 8),
    ([1, 2, 4], 3, 6)
])

def test_missingElementInSortedArray1060(nums, k, expected):
    m = MediumSolution()
    result = m.missingElementInSortedArray1060(nums, k)
    assert result == expected


@pytest.mark.parametrize("nums, expected_peaks", [
    ([1, 2, 3, 1], [2]),
    ([1, 2, 1, 3, 5, 6, 4], [1, 5])
])

def test_findPeakElement162(nums, expected_peaks):
    m = MediumSolution() 
    result = m.findPeakElement162(nums)
    assert result in expected_peaks