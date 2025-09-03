import pytest
from collections import deque
from BFSMedium import TreeNode, Node, mediumSolution
 
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

def serialize_with_next(root):
    """Serialize using next pointers, with '#' marking end of each level."""
    if not root:
        return []

    output = []
    leftmost = root
    while leftmost:
        curr = leftmost
        while curr:
            output.append(curr.val)
            curr = curr.next
        output.append("#")
        leftmost = leftmost.left
    return output


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


@pytest.mark.parametrize("root_list, expected", [
    ([3, 9, 20, None, None, 15, 7], [[3],[20,9],[15,7]]),
    ([1], [[1]]),
    ([], [])
])
def test_zigzagLevelOrder103(root_list, expected):
    root = build_tree(root_list)
    m = mediumSolution()
    result = m.zigzagLevelOrder103(root)
    assert result == expected  


@pytest.mark.parametrize("root_list, expected", [
    ([1,7,0,7,-8,None,None], 2),

])
def test_maxLevelSum1161(root_list, expected):
    root = build_tree(root_list)
    m = mediumSolution()
    result = m.maxLevelSum1161(root)
    assert result == expected  


@pytest.mark.parametrize("tree_builder, expected",  [
        (
            lambda: Node(1,
                         left=Node(2, left=Node(4), right=Node(5)),
                         right=Node(3, left=Node(6), right=Node(7))),
            [1, "#", 2, 3, "#", 4, 5, 6, 7, "#"]
        ),
        (
            lambda: None,
            []
        ),
])
def test_populatingNextRightPointersinEachNode116(tree_builder, expected):
    tree = tree_builder() # lambda: ... is the tree_builder.
    m = mediumSolution()
    root = m.populatingNextRightPointersinEachNode116(tree)
    result = serialize_with_next(root)
    assert result == expected


@pytest.mark.parametrize("root_list, expected", [
        ([1,2,3,None,5,None,4], [1,3,4]),
        ([1,2,3,4,None,None,None,5], [1,3,4,5]),
        ([1,None,3], [1,3]), 
        ([], []), 
])
def test_rightSideView199(root_list, expected):
    # root = build_tree_from_list(values)
    root = build_tree(root_list)
    m = mediumSolution()
    result= m.rightSideView199(root)
    assert result == expected