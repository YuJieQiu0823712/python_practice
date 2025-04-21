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


    def addStrings415(self, num1: str, num2: str) -> str:
        num1_ptr = len(num1) - 1
        num2_ptr = len(num2) - 1
        res = []
        carry = 0
        while num1_ptr >= 0 or num2_ptr >= 0 or carry > 0:
            if num1_ptr >= 0:
                carry += (ord(num1[num1_ptr]) - ord('0'))
                num1_ptr -= 1
            if num2_ptr >= 0:
                carry += (ord(num2[num2_ptr]) - ord('0'))
                num2_ptr -= 1
            res += str(carry % 10) 
            # if you use res='' and return result[::-1]
            # => TC: O(n) - because string is immutable
            # total TC: O(n^2) - n is the length of the longest string
            carry //= 10

        # 1
        return ''.join(result[::-1])
        # TC: O(max(num1,num2)) - n is the length of the longest string
        # SC: O(1)

        # 2
        # revert = []
        # for char in res:
        #     revert.append(char)
        # return ''.join(revert)
        # TC: O(max(num1,num2)) 
        # SC: O(max(num1,num2)) - n is the length of the longest string

        # 3
        # re_length = len(res)
        # res2 = ''
        # for i in range(res_length):
        #     res2 += res[res_length -1 - i]
        # return res2
        # TC: O(max(num1,num2))
        # SC: O(max(num1,num2))
    # Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
    # You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
    # You must also not convert the inputs to integers directly.
    # Input: num1 = "11", num2 = "123"
    # Output: "134"


e = EasySolutions()
sol1 = e.validParentheses20("()[]{}")
print(sol1)