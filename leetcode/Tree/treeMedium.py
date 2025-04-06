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



m = mediumSolution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol1 = m.BinaryTreeLevelOrderTraversal102(root)
print(sol1)

