
import pytest
from throwAwayPython.myFuns import *


# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5


def test_another():
    assert add_numbers(4, 5) == 9