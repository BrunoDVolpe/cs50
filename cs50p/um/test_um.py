from um import count

def test_alone():
    assert count('um') == 1
    assert count('UM') == 1

def test_case():
    assert count('um, UM, Um, uM') == 4

def test_positioning():
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
    assert count("Thanks for the, um, album") == 1
    assert count("Thanks for the album, um") == 1

def test_words():
    assert count("yummy") == 0
    assert count("album") == 0