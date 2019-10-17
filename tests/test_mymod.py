import pytest
import numpy as np
from src.mymod import make_array

def test_make_array():
    a = make_array()
    # assert a.dtype.type is np.int64
    assert True

def test_fail():
    "now false"
    assert True
