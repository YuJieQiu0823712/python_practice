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
