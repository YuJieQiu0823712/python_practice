class EasySolutions:
    def validParentheses20(self, s: str) -> bool:
        stack = []
        lookup = {"(":")", "{":"}", "[":"]"}

        for symbol in s:
            if symbol in lookup:
                stack.append(symbol)
            # else:
            #     stack_pop = stack.pop()
            #     if c != lookup[stack_pop]:
            #         return False
            elif len(stack) == 0 or lookup[stack.pop()] != symbol:
                return False
                # ")" => stack=[] => return False
        # return True
        return len(stack) == 0
        # if stack is empty, all brackets are closed and matched, otherwise return False

    # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    # An input string is valid if:
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.
    # Every close bracket has a corresponding open bracket of the same type.

    # Example 1:
    # Input: s = "()[]{}"
    # Output: true
    # Example 2:
    # Input: s = "(]"
    # Output: false
    
    # TC: O(n) - n is the length of the string s
    # SC: O(n) - n is the length of the stack



e = EasySolutions()
sol1 = e.validParentheses20("()[]{}")
print(sol1)