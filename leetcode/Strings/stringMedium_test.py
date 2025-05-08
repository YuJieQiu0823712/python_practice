from stringMedium import MediumSolution
from stringMedium import DesignAddAndSearchWordsDataStructure211

def test_longestPalindromicSubstring5():
    m = MediumSolution()
    assert m.longestPalindromicSubstring5("babad") == "bab"
    assert m.longestPalindromicSubstring5("cbbd") == "bb"
    assert m.longestPalindromicSubstring5("madamimadam") == "madamimadam"

def test_minimumRemoveToMakeValidParentheses1249():
    m = MediumSolution()
    assert m.minimumRemoveToMakeValidParentheses1249("lee(t(c)o)de)") == "lee(t(c)o)de"
    assert m.minimumRemoveToMakeValidParentheses1249("a)b(c)d") == "ab(c)d"
    assert m.minimumRemoveToMakeValidParentheses1249("))((") == ""

def test_DesignAddAndSearchWordsDataStructure211():
    lookup = DesignAddAndSearchWordsDataStructure211()
    lookup.addWord("bad")
    lookup.addWord("dad")
    lookup.addWord("mad")
    assert lookup.search("pad") == False
    assert lookup.search("bad") == True
    assert lookup.search(".ad") == True
    assert lookup.search("b..") == True

def test_minimumAddToMakeParenthesesValid921():
    m = MediumSolution()
    assert m.minimumAddToMakeParenthesesValid921("())") == 1
    assert m.minimumAddToMakeParenthesesValid921("(((") == 3

def test_basicCalculatorII227():
    m = MediumSolution()
    assert m.basicCalculatorII227("3/2") == 1
    assert m.basicCalculatorII227("14-3 /2+5*2") == 23