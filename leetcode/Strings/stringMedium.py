class MediumSolution(object):
    def longestPalindromicSubstring5(self, s: str) -> str:
        """
        Finds the longest palindromic substring in a given string `s`.

        A palindrome is a string that reads the same backward as forward.
        This function uses the "expand around center" technique to check for palindromes
        by considering each character (and each pair of characters) as potential centers.

        Parameters
        ----------
        s : str
            The input string consisting of digits and/or English letters.

        Returns
        -------
        str
            The longest palindromic substring found in `s`.

        Constraints
        -----------
        - 1 <= len(s) <= 1000
        - s consists only of digits and English letters.

        # TC: O(n^2) - n is the length of s, for each character, we expand around it to find the longest palindrome
        # SC: O(1) - no extra space used, only variables for the longest palindrome and the left and right pointers
        """
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

    def minimumRemoveToMakeValidParentheses1249(self, s: str) -> str:
        s_list = list(s)
        flag = 0
        for i in range(len(s_list)):
            if s_list[i] == "(":
                flag += 1
            elif s_list[i] == ")":
                if flag > 0:
                    flag -= 1
                else:
                    s_list[i] = ""
        flag = 0
        for i in range(len(s_list)-1,-1,-1):
            if s_list[i] == ")":
                flag += 1
            elif s_list[i] == "(":
                if flag > 0:
                    flag -= 1 
                else:
                    s_list[i] = ""
        return "".join(s_list)
    
class DesignAddAndSearchWordsDataStructure211():
    """
    Your WordDictionary object will be instantiated and called as such:
    obj = WordDictionary()
    obj.addWord(word)
    param_2 = obj.search(word)
    """
    def __init__(self):
        self.lookup = {} 


    def addWord(self, word: str) -> None:
        length = len(word)

        if length not in self.lookup:
            self.lookup[length] = [word]
        else:
            self.lookup[length].append(word)


    def search(self, word: str) -> bool:
        length = len(word)
        if length not in self.lookup:
            return False

        for item in self.lookup[length]: 
            matched = False   
            for i in range(length):
                if word[i] == item[i] or word[i] == "." :
                    matched = True
                else:
                    matched = False
                    break
            if matched:
                return True
        return False
         

                

