import collections

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

        TC: O(n^2) - n is the length of s, for each character, we expand around it to find the longest palindrome
        SC: O(1) - no extra space used, only variables for the longest palindrome and the left and right pointers
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
        """
        Removes the minimum number of parentheses to make the input string valid.

        A string is considered valid if:
        - Every opening parenthesis '(' has a corresponding closing parenthesis ')'.
        - Every closing parenthesis ')' has a corresponding opening parenthesis '('.
        - The parentheses are correctly ordered.

        Parameters
        ----------
        s : str
            The input string containing letters and parentheses.

        Returns
        -------
        str
            A valid string with the minimum number of parentheses removed.
       
        TC: O(n)
        SC: O(n) 
        """
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

    def minimumAddToMakeParenthesesValid921(self, s: str) -> int:
        """
        Returns the minimum number of parentheses insertions needed to make the input string valid.
        
        Parameters
        -----------
        s : str
            A string consisting of '(' and ')' characters.

        Returns:
        -----------
        int
            The minimum number of insertions required to make the string valid.

        Constraints
        -----------
            s[i] is either '(' or ')'.

        TC: O(n)
        SC: O(1)     
        """
        open = 0
        close = 0
        for char in s:
            if char == "(":
                open += 1
            elif char == ")" and open > 0:
                open -= 1
            elif char == ")":
                close += 1
        return open + close

    def basicCalculatorII227(self, s: str) -> int:
        """
        Evaluates a basic arithmetic expression given as a string `s` containing non-negative integers,
        operators ('+', '-', '*', '/'), and optional whitespace. The expression is always valid.

        Parameters
        -----------
        s: str
            A valid arithmetic expression string
    
        Returns
        -----------
        int
            The result of evaluating the expression

        TC: O(n)
        SC: O(n) 
        """
        if not s:
            return 0
        
        stack = []
        curr_num = 0
        operator = "+" # s is a valid expression, so the first number in s should be "positive"
        operators = {"+","-","*","/"}
        nums = set(str(x) for x in range(10))

        for idx, char in enumerate(s):
            if char in nums:
                curr_num = curr_num * 10 + (ord(char) - ord("0"))
            if char in operators or idx == len(s)-1:
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
                operator = char
                curr_num = 0
        return sum(stack)

    def groupShiftedStrings249(self, strings: list[str]) -> list[list[str]]:
        """
        Groups shifted strings from the input list.

        Two strings are considered shifted versions of each other if:
            1. They are the same length.
            2. Each character in one string can be shifted by a constant number (modulo 26)
            to get the corresponding character in the other string.
            The shift is cyclic, i.e., after 'z' comes 'a'.
            
        Parameters
        -----------
        strings: List[str]
            A list of lowercase alphabetic strings.

        Returns
        -----------
        List[List[str]]
            A list of grouped lists, where each sublist contains strings that are shifted versions of each other.


        TC: O(n)
        SC: O(n) 
        """
        output = collections.defaultdict(list)

        for string in strings:
            shift_sequence = ()
            for char in string:
                shift_sequence += (ord(char) - ord(string[0])) % 26, # tuple, immutable
            output[shift_sequence].append(string)
        return output.values()


    
class DesignAddAndSearchWordsDataStructure211():
    """
    A data structure that supports adding words and searching for words, 
    including wildcard searches using the '.' character.

    TC: O(n)
    SC: O(n) 
    """
    def __init__(self):
        """
        Initializes an empty lookup dictionary to store words grouped by their lengths.
        """
        self.lookup = {} 


    def addWord(self, word: str) -> None:
        """
        Adds a word to the data structure.

        Args:
            word (str): The word to add.
        """
        length = len(word)

        if length not in self.lookup:
            self.lookup[length] = [word]
        else:
            self.lookup[length].append(word)


    def search(self, word: str) -> bool:
        """
        Searches for a word in the data structure. The word may contain '.' characters
        as wildcards that match any letter.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word is found (considering '.' as a wildcard), False otherwise.
        """
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
         

                

