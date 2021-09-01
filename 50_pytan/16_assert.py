import pytest

def my_func(a,b):
    return a+b


class Tests:
    def test_one(self):
        assert my_func(2,2) == 4

