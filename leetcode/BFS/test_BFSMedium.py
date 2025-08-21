import pytest
from collections import deque
from BFSMedium import TreeNode, mediumSolution
 
def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


@pytest.mark.parametrize("root_list, expected", [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], [])
])
def test_levelOrder102(root_list, expected):
    root = build_tree(root_list)
    m = mediumSolution()
    result = m.levelOrder102(root)
    assert result == expected


@pytest.mark.parametrize("root_list, expected", [
        ([3, 9, 20, None, None, 15, 7], [[15,7],[9,20],[3]]),
        ([1], [[1]]),
        ([], [])
])
def test_levelOrderBottom107(root_list, expected):
    root = build_tree(root_list)
    m = mediumSolution()
    result = m.levelOrderBottom107(root)
    assert result == expected