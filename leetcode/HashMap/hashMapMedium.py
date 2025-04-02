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
        # 3. Generate a Unique Key (Tuple is immutable) for Each Word:
        #   Compute the shift sequence as a tuple of differences between characters. 
        # 4. Efficient Iteration Over Strings:
        #   Iterate over the list and compute the shift sequence.
        #   Store strings in the dictionary based on their computed sequence.
        output = defaultdict(list) # If shift_sequence does not exist, defaultdict(list) creates an empty list automatically
                                   # You don't need to check if the key exists before adding values.

        for string in strings:
            shift_sequence = ()
            for char in string:
                shift_sequence += (ord(char) - ord(string[0])) % 26, # With the comma, it becomes a single-element tuple
                                # ord() => convert str to int (a=97, z=122)
            output[shift_sequence].append(string)

        return list(output.values())
    # Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". 
    # We can keep "shifting" which forms the sequence: "abc" -> "bcd" -> ... -> "xyz"
    # Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

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

    def ContinuousSubarraySum523(self, nums: list[int], k: int) -> bool:
        lookup = {0: -1}
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            mod = curr_sum % k
            if mod in lookup:
                if i - lookup[mod] >= 2:
                    return True
                else:
                    lookup[mod] = i
        return False
        # Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
        # A good subarray is a subarray where:
        # its length is at least two, and
        # the sum of the elements of the subarray is a multiple of k.
        # Note that:
        # A subarray is a contiguous part of the array.
        # An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

        # Input: nums = [23,2,4,6,7], k = 6
        # Output: true
        # Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
        
        # TC: O(n) 
        # SC: O(n) 


m = mediumSolution()
sol1 = m.groupStrings249(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
sol2 = m.ContinuousSubarraySum523([23,2,4,6,7],6)
print(sol1)
print(sol2)


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
    # TC: O(n)
    # SC: O(n) 


vec1 = SparseVector1570([1,0,0,2,3])
vec2 = SparseVector1570([0,3,0,4,0])
print(vec1.dotProduct(vec2)) 


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache146:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    def _add_node(self, node):
        previous_node = self.tail.prev
        previous_node.next = node
        node.prev = previous_node
        node.next = self.tail
        self.tail.prev = node
    def _remove_node(self, node):
        previous_node = node.prev
        previous_node.next = node.next
        node.next.prev = previous_node
    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        node = self.lookup[key]
        self._remove_node(node)
        self._add_node(node)
        return node.val
    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self._remove_node(self.lookup[key])
        elif self.capacity == len(self.lookup):
            lru = self.head.next
            self._remove_node(lru)
            del self.lookup[lru.key]
        new_node = Node(key, value)
        self._add_node(new_node)
        self.lookup[new_node.key] = new_node
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4


lRUCache = LRUCache146(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2) 
print(lRUCache.get(1)) 
lRUCache.put(3, 3)
print(lRUCache.get(2))
lRUCache.put(4, 4) 
print(lRUCache.get(1)) 
print(lRUCache.get(3))  
print(lRUCache.get(4))