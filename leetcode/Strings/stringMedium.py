class MediumSolution(object):
    def longestPalindromicSubstring5(self, s: str) -> str:
        longest = ""
        def helper(s,left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left +1: right]

        for i in range(len(s)):
            word1 = helper(s, i, i)
            if len(word1) > len(longest):
                longest = word1
            word2 = helper(s, i, i+1)
            if len(word2) > len(longest):
                longest = word2
        return longest 

    # Given a string s, return the longest palindromic substring in s.
    # Input: s = "babad"
    # Output: "bab"
    # Explanation: "aba" is also a valid answer.

    # Constraints:
    # 1 <= s.length <= 1000
    # s consist of only digits and English letters.

    # TC: O(n^2) - n is the length of s, for each character, we expand around it to find the longest palindrome
    # SC: O(1) - no extra space used, only variables for the longest palindrome and the left and right pointers

m = MediumSolution()
sol1 = m.longestPalindromicSubstring5("babad")
print(sol1)