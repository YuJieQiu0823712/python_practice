class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class HardSolution:
    def maxPathSum124(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        def find_max(self, node):
            if not node:
                return 0
            left = find_max(self, node.left)
            right = find_max(self, node.right)
            self.max_sum = max(self.max_sum, node.val + left + right)
            return node.val + max(left, right)
        find_max(self, root)
        return self.max_sum
            