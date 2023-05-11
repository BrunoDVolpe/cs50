from plates import is_valid

def test_letters():
    assert is_valid("FFFFFF") == True
    assert is_valid("ffffff") == True
    assert is_valid("FF") == True
    assert is_valid("FFff") == True

def test_with_num():
    assert is_valid("111") == False
    assert is_valid("11") == False
    assert is_valid("F11") == False
    assert is_valid("FFF111") == True
    assert is_valid("FFF100") == True
    assert is_valid("FF1") == True
    assert is_valid("FF11") == True

def test_zero():
    assert is_valid("FFF000") == False

def test_mix_letter_end():
    assert is_valid("FF111F") == False

def test_lenth():
    assert is_valid("F") == False
    assert is_valid("FFF1111") == False

def test_punctuation():
    assert is_valid("FF111.") == False
    assert is_valid("FF111 ") == False
    assert is_valid("FF111!") == False