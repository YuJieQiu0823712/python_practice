
class EasySolution(object):
    """
    A class used to represent easy level solutions.
    """
    def verifyingAnAlienDictionary953(self, words: list[str], order: str) -> bool:
        # Create a lookup dictionary
        # Compare each pair of adjacent words
        # Compare characters one by one
        # If all comparisons pass, return true
        lookup = {}
        for idx, char in enumerate(order):
            lookup[char] = idx
        for word1, word2 in zip(words,words[1:]):
            if word1[:len(word2)] == word2 and len(word1) > len(word2):
                return False
            for char1, char2 in zip(word1,word2):
                if lookup[char1] > lookup[char2]:
                    return False
                elif lookup[char1] < lookup[char2]:
                    break
        return True       
    # sorted lexicographically in this alien language.

    # Example 1:
    # Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    # Output: true
    # Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
    
    # Example 2:
    # Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    # Output: false
    # Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
    
    # Example 3:
    # Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    # Output: false
    # Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character 

    #    creating lookup   comparing words
    # TC:   O(1)                O(n)
    # SC:   O(1)                O(1)
    


e = EasySolution()
sol1 = e.verifyingAnAlienDictionary953(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")

print(sol1)