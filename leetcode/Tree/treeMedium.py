import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val: int=0, left: 'Node'=None, right: 'Node'=None, next: 'Node'=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
    
    def __repr__(self):
        return f"{self.val}"
        
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
            stack.append((root.right, root.val, highest))
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

    def PopulatingNextRightPointersInEachNode116(self, root: 'Node') -> 'Node': 
        # TreeNode => Refers to the actual class object TreeNode. It must already be defined before it’s used in type hints.
        #            Works when the class you're referring to has already been parsed by Python.
        # 'Node' => It's a forward reference — a string that delays the evaluation of the type. Useful when a class refers to itself or a class defined later.
        #            Recommended when writing recursive data structures (like trees, linked lists).
        # Base case
        if not root or not root.left:
            return root
        
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.PopulatingNextRightPointersInEachNode116(root.left)
        self.PopulatingNextRightPointersInEachNode116(root.right)
        return root
    # Input: root = [1,2,3,4,5,6,7]
    # Output: [1,#,2,3,#,4,5,6,7,#]
    # Explanation: Given the above perfect binary tree, your function should populate each next pointer to point to its next right node, 
    # just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
    #         1 ---> Null   (Figure B)
    #       /    \
    #     2  -->  3 --> Null
    #   /  \     /  \
    #  4 -> 5 -> 6 -> 7 --> Null
    # TC: O(log(n)), n is the number of nodes, recursion
    # SC: O(n), n is the number of nodes
    
    def PopulatingNextRightPointersInEachNodeII117(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = collections.deque()
        queue.append(root)
        while queue:
            size_queue = len(queue)
            for i in range(size_queue):
                node = queue.popleft()
                if i < size_queue - 1: 
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
    

m = mediumSolution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol1 = m.BinaryTreeLevelOrderTraversal102(root)
sol2 = m.ValidateBinarySearchTree98(root)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
output3 = m.PopulatingNextRightPointersInEachNode116(n1)
sol3 = print_tree_with_next(n1)

nn1 = Node(1)
nn2 = Node(2)
nn3 = Node(3)
nn4 = Node(4)
nn5 = Node(5)
nn7 = Node(7)
nn1.left = nn2
nn1.right = nn3
nn2.left = nn4
nn2.right = nn5
nn3.right = nn7
output4 = m.PopulatingNextRightPointersInEachNodeII117(nn1)
sol4 = print_tree_with_next(nn1)


print(sol1)
print(sol2)
print(sol3)
print(sol4)

