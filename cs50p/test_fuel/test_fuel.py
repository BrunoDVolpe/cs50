import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50
    assert convert("0/1") == 0
    assert convert("10/20") == 50
    with pytest.raises(ValueError):
        convert("12/")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("cat_dog")
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(2) == "2%"
    with pytest.raises(TypeError):
        gauge("cat")
    with pytest.raises(TypeError):
        gauge("50")