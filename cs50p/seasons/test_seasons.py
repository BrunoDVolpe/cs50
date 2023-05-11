import pytest
import seasons
from seasons import calculate

def test_correct():
    assert calculate("2021-11-08") == "five hundred twenty-five thousand, six hundred"
    assert calculate("2020-11-08") == "one million, fifty-one thousand, two hundred"

def test_incorret_1():
    with pytest.raises(ValueError):
        assert calculate("2021/11/08")

def test_incorret_2():
    with pytest.raises(ValueError):
        assert calculate("08/11/2021")

def test_incorret_3():
    with pytest.raises(ValueError):
        assert calculate("2021/08/11")

def test_incorret_4():
    with pytest.raises(ValueError):
        assert calculate("January 1, 1999")

def test_incorret_5():
    with pytest.raises(ValueError):
        assert calculate("20211108")

def test_incorret_6():
    with pytest.raises(ValueError):
        assert calculate("2021-W01-1")