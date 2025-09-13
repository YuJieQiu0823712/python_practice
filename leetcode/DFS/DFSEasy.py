class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class EasySolution:
    def PathSumI112(self, root: TreeNode, targetSum: int) -> bool:
        """
        TC: O(n), n is the number of nodes in the tree
        SC: O(n)
        """
        if not root:
            return False

        # Base case
        if not root.left and not root.right and root.val == targetSum:
            return True

        return self.PathSumI112(root.left, targetSum - root.val) or self.PathSumI112(root.right, targetSum - root.val)


    def binaryTreePaths257(self, root: TreeNode) -> list[str]:
        """
        TC: O(n)
        SC: O(n), if balanced tree => O(log n)
        """
        def find_path(node, paths, all_path):
            if not node:
                return
            paths.append(str(node.val))

            if not node.left and not node.right:
                all_path.append("->".join(paths))
            find_path(node.left, paths, all_path)
            find_path(node.right, paths, all_path)
            paths.pop()
        all_path = []
        find_path(root, [], all_path)
        return all_path
    
    def diameterOfBinaryTree543(self, root: TreeNode) -> int:
        """
        TC: O(n) where n is the number of nodes in the tree
        SC: O(h) where h is the height of the tree
        """
        self.diameter = 0
        def find_diameter(node):
            if not node:
                return 0
            left = find_diameter(node.left)
            right = find_diameter(node.rght)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        find_diameter(root)
        return self.diameter