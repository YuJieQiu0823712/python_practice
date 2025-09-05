class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class EasySolution:
    def hasPathSum112(self, root: TreeNode, targetSum: int) -> bool:
        """
        TC: O(n), n is the number of nodes in the tree
        SC: O(h), h is the height of the tree
        """
        if not root:
            return False

        # Base case
        if not root.left and not root.right and root.val == targetSum:
            return True

        return self.hasPathSum112(root.left, targetSum - root.val) or self.hasPathSum112(root.right, targetSum - root.val)