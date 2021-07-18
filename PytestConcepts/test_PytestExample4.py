import pytest as pytest


@pytest.fixture(scope='module')
def beforeClass():
    print('Before a Class')
    yield
    print('After Class')

@pytest.fixture()
def beforeMethod():
    print('Before a Method')
    yield
    print('After Method')

def test_methodA(beforeMethod, beforeClass):
    print("This is method A")

def test_methodB(beforeMethod, beforeClass):
    print("This is method B")