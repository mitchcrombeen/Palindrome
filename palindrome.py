""""Check whether a string is a palindrome"""

def is_palindrome(phrase):
    """Return True if a text reads the same forwards and backwards"""
    if not isinstance(phrase,str):
        raise ValueError("The phrase must be a string")
