from dynamicProgrammingMedium import MediumSolution

def test_wordBreak139():
    m = MediumSolution()
    assert m.wordBreak139("leetcode", ["leet","code"]) == True
    assert m.wordBreak139("catsandog", ["cats","dog","sand","and","cat"]) == False
