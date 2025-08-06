import pytest
from stackMedium import MediumSolution, TreeNode, BinarySearchTreeIterator173, constructBinaryTreeFromString536

# Helper to build BST from level-order list
def build_bst_from_level_order(values):
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

# Helper to convert tree to list (preorder)
def tree_to_list(root):
    if not root:
        return []
    result = [root.val]
    result += tree_to_list(root.left)
    result += tree_to_list(root.right)
    return result



@pytest.mark.parametrize("commands, arguments, expected", [
    (
        ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"],
        [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []],
        [None, 3, 7, True, 9, True, 15, True, 20, False]
    )
])
def test_bst_iterator173(commands, arguments, expected):
    results = []
    bst_iterator = None

    for cmd, arg in zip(commands, arguments):
        if cmd == "BSTIterator":
            root = build_bst_from_level_order(arg[0])
            bst_iterator = BinarySearchTreeIterator173(root)
            results.append(None)
        elif cmd == "next":
            results.append(bst_iterator.next())
        elif cmd == "hasNext":
            results.append(bst_iterator.hasNext())

    assert results == expected


@pytest.mark.parametrize("input_str, expected", [
    ("4(2(3)(1))(6(5))", [4, 2, 3, 1, 6, 5]),
    ("4(2(3)(1))(6(5)(7))", [4, 2, 3, 1, 6, 5, 7])
])
#         4
#       /   \
#      2     6
#     / \   /
#    3   1 5
def test_str2tree536(input_str, expected):
    solver = constructBinaryTreeFromString536()
    root = solver.str2tree(input_str)
    result = tree_to_list(root)
    assert result == expected


@pytest.mark.parametrize("pushed, popped, expected", [
        ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
        ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False)
])
def test_validateStackSequences946(pushed, popped, expected):
    m = MediumSolution()
    result = m.validateStackSequences946(pushed, popped)
    assert result == expected


@pytest.mark.parametrize("expression, expected", [
    ("3+2*2", 7),
    (" 3/2 ", 1),
    (" 3+5 / 2 ", 5)
])
def test_basicCalculatorII227(expression, expected):
    m = MediumSolution()
    result = m.basicCalculatorII227(expression)
    assert result == expected


@pytest.mark.parametrize("asteroids, expected", [
    ([5, 10, -5], [5, 10]),
    ([8, -8], [])

])
def test_asteroidCollision735(asteroids, expected):
    m = MediumSolution()
    result = m.asteroidCollision735(asteroids)
    assert result == expected


