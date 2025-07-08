class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class EasySolution:
    def closestBinarySearchTreeValue270(self, root: TreeNode, target: float) -> int:
        """
        Finds the value in a Binary Search Tree that is closest to the target.

        Args:
            root (TreeNode): The root of the binary search tree.
            target (float): The target value to find the closest match for.

        Returns:
            int: The value in the BST that is closest to the target.
        """
        res = root.val
        while root:
            if abs(target - root.val) < abs(target - res):
                res = root.val
            if root.val < target:
                root = root.right
            else:
                root = root.left
        return res
