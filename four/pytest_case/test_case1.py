import pytest


def func(x):
    return x+1

def test_func():
    assert func(4) == 5

@pytest.mark.parametrize('a,b', [(1,2),(3,3)])
def test_func2(a, b):
    assert  func(a) == b





if __name__ == '__main__':
    pytest.main(['test_case1.py','-v'])