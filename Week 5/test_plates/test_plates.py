import pytest
from plates import is_valid

def main():
    test_length()
    test_start()
    test_numbers()
    test_characters()

def test_length():
    assert is_valid("a") == False
    assert is_valid("ab") == True
    assert is_valid("abcdef") == True
    assert is_valid("abcdefg") == False

def test_start():
    assert is_valid("12") == False
    assert is_valid("a1") == False
    assert is_valid("ab1") == True

def test_numbers():
    assert is_valid("ab01") == False
    assert is_valid("ab10") == True
    assert is_valid("ab10c") == False

def test_characters():
    for char in ",<.>/?;:'-_=+`~\\|)(][}{)&*^%$#@!":
        assert is_valid(f"ab10{char}") == False

if __name__ == "__main__":
    main()       