import pytest

def test_method1():
    x=5
    y=10
    z=2
    assert y>x>z

def test_method2():
    x=10
    y=20
    z=25
    assert y+10>z>x
