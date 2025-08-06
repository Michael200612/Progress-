import pytest
from twttr import shorten

def main():
    test_lower()
    test_upper()

def test_lower():
    assert shorten("qwertyuiopasdfghjklzxcvbnm") == "qwrtypsdfghjklzxcvbnm"

def test_upper():
    assert shorten("QWERTYUIOPASDFGHJKLZXCVBNM") == "QWRTYPSDFGHJKLZXCVBNM"

if __name__ == "__main__":
    main()