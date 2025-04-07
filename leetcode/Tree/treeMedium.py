import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class mediumSolution:
    def BinaryTreeLevelOrderTraversal102(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
            
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            curr_list = []
            for i in range(len(queue)):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                curr_list.append(curr_node.val) #
            res.append(curr_list)
        return res
    # Given the root of a binary tree, return the level order traversal of its nodes' values.
    # Input: root = [3,9,20,null,null,15,7]
    # Output: [[3],[9,20],[15,7]] 
    #     3         level 1
    #   /   \  
    #  9    20      level 2
    #     /    \ 
    #    15     7   level 3
    # TC: O(n) 
    # SC: O(n) 


    # 1. Iterative
    def ValidateBinarySearchTree98(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, lowest, highest = stack.pop()
            if not root:
                continue
            if root.val <= lowest or root.val >= highest:
                return False
            stack.append((root.left, lowest, root.val))
            stack.append((root.right, root.val, hightst))
        return True
        # TC: O(n) 
        # SC: O(n) stack
        
    # 2. Recursive
    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid(root, float('-inf'), float('inf'))
        
    def is_valid(self, root, lowest, highest):
        if not root: 
            return True
        if root.val <= lowest or root.val >= highest:
            return False
        return self.is_valid(root.left, lowest, root.val) and self.is_valid(root.right, root.val, highest)
    # TC: O(n) 
    # SC: O(n) call stack

    # Given the root of a binary tree, determine if it is a valid binary search tree (BST).
    # A valid BST is defined as follows:
    # The left subtree of a node contains only nodes with keys less than the node's key.
    # The right subtree of a node contains only nodes with keys greater than the node's key.
    # Both the left and right subtrees must also be binary search trees.
    
    # Input: root = [5,1,4,null,null,3,6]
    # Output: false
    # Explanation: The root node's value is 5 but its right child's value is 4.


m = mediumSolution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol1 = m.BinaryTreeLevelOrderTraversal102(root)
print(sol1)

