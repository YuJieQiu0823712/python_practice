import pytest
from binarySearchEasy import TreeNode, EasySolution

def build_bst_from_list(vals):
    """Helper function to build BST from a list of values."""
    if not vals:
        return None

    root = TreeNode(vals[0])
    for val in vals[1:]:
        insert_into_bst(root, val)
    return root

def insert_into_bst(root, val):
    if val < root.val:
        if root.left:
            insert_into_bst(root.left, val)
        else:
            root.left = TreeNode(val)
    else:
        if root.right:
            insert_into_bst(root.right, val)
        else:
            root.right = TreeNode(val)

@pytest.mark.parametrize("bst_vals, target, expected", [
    ([4, 2, 5, 1, 3], 3.71, 4),
    ([1], 4.42, 1)
])

def test_closestBinarySearchTreeValue270(bst_vals, target, expected):
    e = EasySolution()
    root = build_bst_from_list(bst_vals)
    result = e.closestBinarySearchTreeValue270(root, target)
    assert result == expected
