from dynamicProgrammingMedium import MediumSolution

def test_wordBreak139():
    m = MediumSolution()
    assert m.wordBreak139("leetcode", ["leet","code"]) == True
    assert m.wordBreak139("catsandog", ["cats","dog","sand","and","cat"]) == False

def test_twoKeysKeyboard650():
    m = MediumSolution()
    assert m.twoKeysKeyboard650(3) == 3
    assert m.twoKeysKeyboard650(9) == 6

def test_maximumNumberOfPointsWithCost1937():
    m = MediumSolution()
    assert m.maximumNumberOfPointsWithCost1937([[1,2,3],[1,5,1],[3,1,1]]) == 9
    assert m.maximumNumberOfPointsWithCost1937([[1,5],[2,3],[4,2]]) == 11