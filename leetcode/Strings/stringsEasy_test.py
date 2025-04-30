from stringsEasy import EasySolutions

def test_validParentheses20() :
    e = EasySolutions()
    assert e.validParentheses20("()[]{}") == True
    assert e.validParentheses20("(]") == False
    assert e.validParentheses20("([{}])") == True
    assert e.validParentheses20("(((") == False


def test_addStrings415():
    e = EasySolutions()
    assert e.addStrings415("11", "123") == "134"
    assert e.addStrings415("456", "77") == "533"
    assert e.addStrings415("0", "0") == "0"