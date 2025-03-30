import array

# class mediumSolution(object):
    

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
