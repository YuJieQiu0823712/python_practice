from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTreeIterator173:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        return_node = self.stack.pop()
        next_node = return_node.right
        while next_node:
            self.stack.append(next_node)
            next_node = next_node.left
        return return_node.val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0


class MediumSolution:
    def validateStackSequences946(self, pushed: list[int], popped: list[int]) -> bool:
        pop_idx = 0
        stack = []
        for value in pushed:
            stack.append(value)
            while stack and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1
        return not stack