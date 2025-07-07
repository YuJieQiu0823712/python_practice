class EasySolution:

    def validPalindrome125(self, s: str) -> bool:
        """
        Checks if the given string is a valid palindrome, considering only alphanumeric characters and ignoring case.

        Args:
            s (str): The input string to check.

        Returns:
            bool: True if the string is a valid palindrome, False otherwise.

        TC: O(n)
        SC: O(1) 
        """
        left = 0
        right = len(s) -1
        s = s.lower()

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    
    def reverseOnlyLetters917(self, s: str) -> str:
        """
        Reverses only the letters in a string, keeping all non-letter characters in their original positions.

        Args:
            s (str): The input string to reverse letters in.
        
        Returns:
            str: The string with only letters reversed, while non-letter characters remain in their original positions.
        
        TC: O(n)
        SC: O(n) 
        """
        # edge case
        if not s:
            return None
        # raise Exception("input cannot be None")
        
        s_list = list(s)
        left = 0
        right = len(s_list) - 1
        while left < right:
            while left < right and not s_list[left].isalpha():
                left += 1
            while left < right and not s_list[right].isalpha():
                right -= 1
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return "".join(s_list)

