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