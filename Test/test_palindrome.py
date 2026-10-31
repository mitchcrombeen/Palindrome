#module for TDD of my palindrome module. Commenting to check if test actions are enabled.
import pytest
from palindrome import is_palindrome

def test_is_palindrome_accepts_one_str():
    with pytest.raises(ValueError):
        is_palindrome(1997)

def test_is_palindrome_returns_false_when_given_empty_str():
    assert is_palindrome('') == False