from app import add

def test_add():
    assert add(10, 20) == 30

def test_negative():
    assert add(-10, 5) == -5

def test_zero():
    assert add(0, 0) == 0