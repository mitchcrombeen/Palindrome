""""Check whether a string is a palindrome"""
from collections import deque

def is_palindrome(phrase):
    """Return True if a text reads the same forwards and backwards"""
    if not isinstance(phrase,str):
        raise ValueError("The phrase must be a string")
    if len(phrase) == 0:
        return False
    word = deque(phrase)
    while len(word) >1:
        left = word.popleft()
        right = word.pop()
        if left != right:
            return False
    return True
