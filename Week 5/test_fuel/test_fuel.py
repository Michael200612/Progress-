import pytest
from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/101") == 0
    assert convert("0/4") == 0
    assert convert("4/4") == 100
    assert convert("1/4") == 25
    with pytest.raises(ValueError):
          convert("cat/dog")
          convert("4/0")
          convert("-1/-4")

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"

if __name__ == "__main__":
    main()