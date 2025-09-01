from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next        

class mediumSolution:
    def levelOrder102(self, root: TreeNode) -> list[list[int]]:
        """
        TC: O(n), n is the number of nodes in the tree
        SC: O(n)
        """
        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)

        while queue:
            queue_len = len(queue)
            curr_list = []

            for _ in range(queue_len):
                node = queue.popleft()
                curr_list.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(curr_list)

        return res
    
    def levelOrderBottom107(self, root: TreeNode) -> list[list[int]]:
        """
        TC: O(n), n is the number of nodes in the tree
        SC: O(n)
        """
        if not root:
            return []
        
        res = deque()
        queue = deque()
        queue.append(root)

        while queue:
            curr_list = []
            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.popleft()
                curr_list.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.appendleft(curr_list)
        return list(res) # convert deque to list

    
    def zigzagLevelOrder103(self, root: TreeNode) -> list[list[int]]:
        """
        TC: O(n), n is the number of nodes in the tree
        SC: O(n)
        """
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        normal_append = True

        while queue:
            queue_len = len(queue)
            curr_list = deque()

            for _ in range(queue_len):
                node = queue.popleft()

                if normal_append:
                    curr_list.append(node.val)
                else:
                    curr_list.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list(curr_list))
            normal_append = not normal_append
        return res


    def maxLevelSum1161(self, root: TreeNode) -> int:
        """
        TC: O(n), n is the number of nodes in the tree
        SC: O(n)
        """
        if not root:
            return 0
        res = [0, float("-inf")]
        level = 0
        queue = deque()
        queue.append(root)
        
        while queue:
            level += 1
            curr_sum = 0
            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.popleft()
                curr_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if curr_sum > res[1]:
                res[0] = level
                res[1] = curr_sum
        return res[0]


    def populatingNextRightPointersinEachNode116(self, root: Node) -> Node:
        """
        TC: O(n), n is the number of nodes in the tree
        SC: O(n)
        """
        if not root:
            return None
        queue = deque()
        queue.append(root)

        while queue:
            prev_node = None
            queue_len = len(queue)
            for _ in range(queue_len):
                curr_node = queue.popleft()
                if prev_node:
                    prev_node.next = curr_node
                prev_node = curr_node

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return root