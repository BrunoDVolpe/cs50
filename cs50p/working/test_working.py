import pytest
from working import convert

def test_AM_to_PM():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"

def test_PM_to_AM():
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"

def test_12s():
    assert convert("12 AM to 12 AM") == "00:00 to 00:00"
    assert convert("12 PM to 12 PM") == "12:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

def test_am_pm():
    with pytest.raises(ValueError):
        convert("12 am to 12 pm")

def test_mins():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")

def test_hours():
    with pytest.raises(ValueError):
        convert("13 PM to 5 PM")

def test_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")