import pytest
from bank import value

def main():
    test_lower()
    test_upper()

def test_lower():
    assert value(" hellothere") == 0
    assert value(" hz") == 20
    assert value(" yo") == 100

def test_upper():
    assert value(" HELLOTHERE") == 0
    assert value(" HZ") == 20
    assert value(" YO") == 100

if __name__ == "__main__":
    main()