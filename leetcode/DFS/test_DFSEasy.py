import pytest
from collections import deque
from DFSEasy import TreeNode, EasySolution
 
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
        ([5,4,8,11,None,13,4,7,2,None,None,None,1], 22, True),
        ([1,2,3], 5, False),
        ([], 0, False)
])
def test_PathSumI112(root_list, targetSum, expected):
    e = EasySolution()
    root = build_tree(root_list)
    result = e.PathSumI112(root, targetSum)
    assert result == expected

@pytest.mark.parametrize("root_list, expected", [
        ([1, 2, 3, None, 5], ["1->2->5", "1->3"]),
        ([1], ["1"]),
        ([], []),
])
def test_binaryTreePaths257(root_list, expected):
    e = EasySolution()
    root = build_tree(root_list)
    result = e.binaryTreePaths257(root)
    assert result == expected