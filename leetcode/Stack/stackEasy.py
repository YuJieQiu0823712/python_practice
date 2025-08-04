class EasySolution:
    def RemoveAllAdjacentDuplicatesInString1047(self,s: str) -> str:
        """
        TC: O(n)
        SC: O(n)
        """
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

