import pytest
from twoPointerEasy import EasySolution

@pytest.mark.parametrize("s, expected", [
    ("A man, a plan, a canal: Panama", True), # Palindrome ignoring punctuation and spaces
    ("race a car", False), # Not a palindrome
    (" ", True), # s is an empty string "" after removing non-alphanumeric characters.
                 # Since an empty string reads the same forward and backward, it is a palindrome.
])

def test_validPalindrome125(s, expected):
    m = EasySolution()
    result = m.validPalindrome125(s)
    assert result == expected


@pytest.mark.parametrize("s, expected", [
    ("ab-cd", "dc-ba"), # Reverse only letters, ignore dashes
    ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"), # Reverse only letters, ignore dashes
    ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!") # Reverse only letters, ignore special characters
])

def test_reverseOnlyLetters917(s, expected):
    m = EasySolution()
    result = m.reverseOnlyLetters917(s)
    assert result == expected