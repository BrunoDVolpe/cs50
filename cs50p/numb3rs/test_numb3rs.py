from numb3rs import validate

def test_1digit():
    assert validate("0.0.0.0") == True
    assert validate("5.0.0.9") == True

def test_2digits():
    assert validate("10.10.55.88") == True
    assert validate("10.0.0.88") == True

def test_3digits():
    assert validate("100.10.0.255") == True
    assert validate("255.255.255.255") == True
    assert validate("255.155.0.0") == True

def test_256():
    assert validate("275.3.6.28") == False
    assert validate("0.0.0.256") == False

def test_no_digits():
    assert validate("") == False

def test_more_digits():
    assert validate("0.0.0.0.0") == False

def test_no_numbers():
    assert validate("0.0.0.a") == False