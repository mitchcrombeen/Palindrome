"""Test my is_palindrome function"""
#module for TDD of my palindrome module. Commenting to check if test actions are enabled.
import pytest
from palindrome import is_palindrome

def test_is_palindrome_accepts_one_str():
    """is_palindrome raises a ValueError when not provided with a value that is an;
    instance of str."""
    with pytest.raises(ValueError):
        is_palindrome(1997)

def test_is_palindrome_returns_false_when_given_empty_str():
    """is_palindrome returns False when called with an empty string."""
    assert is_palindrome('') is False

def test_is_palindrome_returns_true_given_a():
    """is_palindrome returns True if called with 'a'."""
    assert is_palindrome("a") is True

def test_is_palindrome_returns_true_given_bb():
    """is_palindrome returns True if called with "bb"."""
    assert is_palindrome("b") is True

def test_is_palindrome_returns_false_given_abc():
    """is_palindrome returns False is called with "abc"."""
    assert is_palindrome("abc") is False
