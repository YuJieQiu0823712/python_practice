import array
from collections import defaultdict

class mediumSolution(object):
    def groupStrings249(self,strings: list[str]) -> list[list[str]]:
        # 1. A string like "abc" and "bcd" share a common shift pattern:
        #   "abc" → (0, 1, 2)
        #   "bcd" → (0, 1, 2)
        #   Both should be grouped together.
        # 2. Use a Dictionary for Grouping:
        #   Use a defaultdict(list) to store words with the same shift pattern.
        # 3. Generate a Unique Key (Tuple) for Each Word:
        #   Compute the shift sequence as a tuple of differences between characters.
        # 4. Efficient Iteration Over Strings:
        #   Iterate over the list and compute the shift sequence.
        #   Store strings in the dictionary based on their computed sequence.
        output = defaultdict(list)

        for string in strings:
            shift_sequence = ()
            for char in string:
                shift_sequence += (ord(char) - ord(string[0])) % 26,
            output[shift_sequence].append(string)

        return list(output.values())
    # Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". 
    # We can keep "shifting" which forms the sequence: "abc" -> "bcd" -> ... -> "xyz"

    # Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
    # Output:
    # [
    # ["abc","bcd","xyz"],
    # ["az","ba"],
    # ["acef"],
    # ["a","z"]
    # ]

    # TC: O(n) 
    # SC: O(n) 

m = mediumSolution()
sol1 = m.groupStrings249(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
print(sol1)

class WordDictionary211:
    def __init__(self):
       self.lookup = {}

    def addWord(self, word: str) -> None:
        length = len(word)
        if length not in self.lookup:
            self.lookup[length] = [word]#
        else:
            self.lookup[length].append(word)

    def search(self, word:str) -> bool:
        length = len(word)
        if length not in self.lookup:
            return False

        for item in self.lookup[length]:
            matched = False
            for i in range(length): 
                if word[i] == item[i] or word[i] == '.':
                    matched = True
                else:
                    matched = False
                    break # check next item
            if matched:
                return True
        return matched
    # Implement the WordDictionary class:
    # WordDictionary() Initializes the object.
    # void addWord(word) Adds word to the data structure, it can be matched later.
    # bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

    # Input
    # ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    # [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    
    # Output
    # [null,null,null,null,false,true,true,true]

    # Explanation
    # WordDictionary wordDictionary = new WordDictionary();
    # wordDictionary.addWord("bad");
    # wordDictionary.addWord("dad");
    # wordDictionary.addWord("mad");
    # wordDictionary.search("pad"); // return False
    # wordDictionary.search("bad"); // return True
    # wordDictionary.search(".ad"); // return True
    # wordDictionary.search("b.."); // return True

    #     addWord     searchWord
    # TC:   O(1)         O(n)  only iterate once
    # SC:   O(n)         O(n)  use dict
    #    map has list

wordDictionary = WordDictionary211()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad")) #return False
print(wordDictionary.search("bad")) #return True
print(wordDictionary.search(".ad")) #return True
print(wordDictionary.search("b..")) #return True


class SparseVector1570:
    def __init__(self,nums: list[int]):
        # store only non-zero value using dictionary {index: value}
        # perform the dot product only on common indices
        self.non_zero = {}
        for idx, val in enumerate(nums):
            if val != 0:
                self.non_zero[idx] = val
    
    def dotProduct(self, vec: 'SparseVector1570') -> int:
        result = 0
        for key, val in (self.non_zero.items()):
            if key in vec.non_zero:
                result += val * vec.non_zero[key] 
        return result
    # Implement class SparseVector:
    # SparseVector(nums) Initializes the object with the vector nums
    # dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
    # A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.
    # Follow up: What if only one of the vectors is sparse?
    
    # Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
    # Output: 8
    # Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
    # v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8


vec1 = SparseVector1570([1,0,0,2,3])
vec2 = SparseVector1570([0,3,0,4,0])
print(vec1.dotProduct(vec2)) 

