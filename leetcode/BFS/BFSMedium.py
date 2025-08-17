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
        queue = collection.deque()
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