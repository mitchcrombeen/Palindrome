from palindrome import is_palindrome

def test_is_palindrome_accepts_one_str():
    with pytest.raises(ValueError):
        is_palindrome(1997)