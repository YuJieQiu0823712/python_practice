import pytest
from collections import deque
from BFSEasy import TreeNode, EasySolution

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

@pytest.mark.parametrize("root_list, expected",[
    ([3, 9, 20, None, None, 15, 7], [3, 14.5, 11])
])

def test_averageOfLevels637(root_list, expected):
    root = build_tree(root_list)
    e = EasySolution()
    result = e.averageOfLevels637(root)
    assert result == expected

@pytest.mark.parametrize("root_list, expected",[
    ([3, 9, 20, None, None, 15, 7], 2)
])

def test_minDepth111(root_list, expected):
    root = build_tree(root_list)
    e = EasySolution()
    result = e.minDepth111(root)
    assert result == expected    