import pytest
from collections import deque
from DFSMedium import TreeNode, MediumSolution
 
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

@pytest.mark.parametrize("root_list, targetSum, expected", [
        ([5,4,8,11,None,13,4,7,2,None,None,5,1], 22, [[5,4,11,2],[5,8,4,5]]),
        ([1,2,3], 5, []),
        ([1,2], 0, [])
])
def test_pathSumII113(root_list, targetSum, expected):
    m = MediumSolution()
    root = build_tree(root_list)
    result = m.pathSumII113(root, targetSum)
    assert result == expected