from twttr import shorten

def test_vowel():
    assert shorten("AaEeIiOoUu") == ""


def test_consonant():
    assert shorten("BbCcDd") == "BbCcDd"


def test_str_number():
    assert shorten("CS50") == "CS50"


def test_mixed():
    assert shorten("Twitter CS50 Python") == "Twttr CS50 Pythn"


def test_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"