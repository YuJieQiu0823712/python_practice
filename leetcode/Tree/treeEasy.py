class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree_with_next(root: 'Node'):
        result = []
        start = root
        while start:
            curr_node = start
            while curr_node:
                result.append(curr_node.val)
                curr_node = curr_node.next
            result.append('#')
            start = start.left
        return result

class easySolution:

    def binaryTreePreorderTraversal144(self, root: TreeNode) -> list[int]:
        # DFS
        # Preorder traversal: node, left, right

        # 1 Iterative
        # if not root:
        #     return  []
        
        # res = []
        # stack = []
        # stack.append(root)
        # while stack:
        #     curr_node = stack.pop()
        #     if curr_node:
        #         res.append(curr_node.val)

        #     if curr_node.right:
        #         stack.append(curr_node.right)
        #     if curr_node.left:
        #         stack.append(curr_node.left)
        # return res
        # TC: O(n) 
        # SC: O(n) Skewed tree: O(n), Balanced tree: O(log n) 

        # 2 Recursive
        res = []
        if not root:
            return []
        
        def helper(node):
            if node:
                res.append(node.val)
                helper(node.left)
                helper(node.right)
        helper(root)
        return res
        # TC: O(n) 
        # SC: O(n) Skewed tree: O(n), Balanced tree: O(log n) 
    # Given the root of a binary tree, return the preorder traversal of its nodes' values.
    # Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
    # Output: [1,2,4,5,6,7,3,8,9]
    # Explanation: 
    #         1
    #       /   \
    #     2       3
    #    / \       \
    #   4   5       8
    #      / \     /
    #     6   7   9

    def binaryTreeInorderTraversal94(self, root: TreeNode) -> list[int]:
        # DFS
        # Inorder traversal: left, node, right
        # 1 Iterative
        # res = []
        # stack = []
        # curr_node = root
        # while curr_node or stack:
        #     while curr_node:
        #             stack.append(curr_node)
        #             curr_node = curr_node.left
        #     curr_node = stack.pop()
        #     res.append(curr_node.val)
        #     curr_node = curr_node.right
        # return res
        # TC: O(n)
        # SC: O(n)      
                
        # 2 Recursive
        res = []
        def helper(node):
            if not node:
                return #
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        helper(root)
        return res
        # TC: O(n)
        # SC: O(n)  

    # Given the root of a binary tree, return the inorder traversal of its nodes' values.
    # Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
    # Output: [4,2,6,5,7,1,3,9,8]
    # Explanation:
    #         1
    #       /   \
    #     2       3
    #    / \       \
    #   4   5       8
    #      / \     /
    #     6   7   9


    def rangeSumofBST938(self, root: TreeNode, low: int, high: int) -> int:
        # BST binary search tree => left < node < right
        # 1 Iterative
        # stack = [root]
        # res = 0
        
        # while stack:
        #     curr_node = stack.pop()
        #     if curr_node:
        #         if curr_node.val >= low and curr_node.val <= high:
        #             res += curr_node.val
        #         if curr_node.val > low:
        #             stack.append(curr_node.left)
        #         if curr_node.val < high:
        #             stack.append(curr_node.right)
        # return res

        # res = 0
        # 2 Recursive
      
        def helper(node):
            
            if not node:
                return 0
            else:
                if node.val >= low and node.val <= high:
                    self.res += node.val
                if node.val > low:
                    helper(node.left)
                if node.val < high:
                    helper(node.right)
                
        self.res = 0 # global variable
        helper(root)
        return self.res
        # TC: O(n)
        # SC: O(n)

    # Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
    # Output: 32
    # Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
    #     10
    #    /  \
    #   5    15
    #  / \     \
    # 3   7     18

    def closestBinarySearchTreeValue270(self,root: TreeNode, target: float) -> int:
        res = root.val
        while root:
            if abs(target - root.val) < abs(target - res):
                res = root.val
            if root.val < target:
                root = root.right
            else:
                root = root.left
        return res

    # Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
    # Given target value is a floating point.
    # You are guaranteed to have only one unique value in the BST that is closest to the target.
    # Input: root = [10,5,15,3,7,null,18], target = 4.71
    # Output: 5
    #     10
    #    /  \
    #   5    15
    #  / \     \
    # 3   7     18
      



e = easySolution()

node6 = TreeNode(6)
node7 = TreeNode(7)
node5 = TreeNode(5, node6, node7)
node4 = TreeNode(4)
node2 = TreeNode(2, node4, node5)
node9 = TreeNode(9)
node8 = TreeNode(8, node9)
node3 = TreeNode(3, None, node8)
node1 = TreeNode(1, node2, node3)

sol1 = e.binaryTreePreorderTraversal144(node1)
sol2 = e.binaryTreeInorderTraversal94(node1)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)
sol3 = e.rangeSumofBST938(root, 7, 15)


sol4 = e.closestBinarySearchTreeValue270(root, 4.71)


print(sol1)
print(sol2)
print(sol3)
print(sol4)
