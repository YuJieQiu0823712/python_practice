from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTreeIterator173:
    """
    TC: O(1)
    SC: O(H), where H is the heigh of the tree
    """
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        return_node = self.stack.pop()
        next_node = return_node.right #
        while next_node:
            self.stack.append(next_node)
            next_node = next_node.left
        return return_node.val
        
    def hasNext(self) -> bool:
        return len(self.stack) > 0


class MediumSolution:
    def validateStackSequences946(self, pushed: list[int], popped: list[int]) -> bool:
        """
        TC: O(n)
        SC: O(n)
        """
        pop_idx = 0
        stack = []
        for value in pushed:
            stack.append(value)
            while stack and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1
        return not stack

    def basicCalculatorII227(self, s: str) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        if not s:
            return 0
        stack = []
        curr_num = 0
        operator = "+"
        operators = {"+","-","*","/"}
        nums = set()
        for i in range(10):
            nums.add(str(i))
        for idx, char in enumerate(s):
            if char in nums:
                curr_num = curr_num * 10 + (ord(char) - ord("0"))
            if char in operators or idx == len(s) - 1:
                if operator == "+":
                    stack.append(curr_num)
                elif operator == "-":
                    stack.append(-curr_num)
                elif operator == "*":
                    temp_num = stack.pop()
                    stack.append(temp_num * curr_num)
                else:
                    temp_num = stack.pop()
                    stack.append(int(temp_num / curr_num))
                curr = 0
                operator = char
        return sum(stack)

    def asteroidCollision735(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                prev_asteroid = stack.pop()
                if prev_asteroid > -asteroid:
                    asteroid = prev_asteroid
                elif prev_asteroid == - asteroid:
                    asteroid = 0
            if asteroid != 0:
                stack.append(asteroid)
        return stack
        