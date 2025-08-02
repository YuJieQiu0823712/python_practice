import pytest
from stackMedium import MediumSolution, TreeNode, BinarySearchTreeIterator173

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


@pytest.mark.parametrize("pushed, popped, expected", [
        ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
        ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False)
])

def test_validateStackSequences946(pushed, popped, expected):
    m = MediumSolution()
    result = m.validateStackSequences946(pushed, popped)
    assert result == expected