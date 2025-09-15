import pytest
from collections import deque
from DFSHard import TreeNode, HardSolution

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

@pytest.mark.parametrize("values, expected", [
        ([1, 2, 3], 6),  
        ([-10, 9, 20, None, None, 15, 7], 42)
])
def test_maxPathSum124(values, expected):
    h = HardSolution()
    root = build_tree(values)
    result = h.maxPathSum124(root)
    assert result == expected