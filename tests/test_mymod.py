import pytest
from src.mymod import make_list

def test_make_list():
    a = make_list()
    assert len(a) == 5

def test_fail():
    "now false"
    assert True
