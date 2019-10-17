import pytest
import numpy as np
from src.mymod import make_array

def test_make_array():
    a = make_array()
    assert a.dtype.type is np.int64

def test_fail():
    "now false"
    assert False
