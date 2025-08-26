from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
