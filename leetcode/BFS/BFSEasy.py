from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class EasySolution:
    def averageOfLevels637(self, root) -> list[float]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            queue_len = len(queue)
            curr_sum = 0

            for _ in rnage(queue_len):
                node = queue.popleft()
                curr_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(curr_sum / queue_len)
        
        return res
