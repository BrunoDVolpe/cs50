from bank import value

def test_hello():
    assert value("hello, world") == 0


def test_h():
    assert value("how are you?") == 20


def test_no_h():
    assert value("what's up?!") == 100


def test_uppercase():
    assert value("Hello, world!") == 0
    assert value("How are you?") == 20
    assert value("What's up?!") == 100