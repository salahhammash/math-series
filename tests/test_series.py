import pytest

from series.series import fibonacci 
from series.series import lucas
from series.series import sum_series

def test_zero():
    actual = fibonacci(0)
    excepted = 0
    assert actual == excepted


def test_one():
    actual = fibonacci(1)
    excepted = 1
    assert actual == excepted    

def test_two():
    actual = fibonacci(2)
    excepted = 1
    assert actual == excepted     
    

def test_three():
    actual = fibonacci(3)
    excepted = 2
    assert actual == excepted         


def test_four():
    actual = fibonacci(4)
    excepted = 3
    assert actual == excepted         


def test_lucas_zero():
    actual = lucas(0)
    excepted = 2
    assert actual == excepted

def test_lucas_one():
    actual = lucas(1)
    excepted = 1
    assert actual == excepted


def test_lucas_tow():
    actual = lucas(2)
    excepted = 3
    assert actual == excepted   

def test_lucas_three():
    actual = lucas(3)
    excepted = 4
    assert actual == excepted   


def test_sum_series():
    actual = sum_series(3)
    excepted = 2
    assert actual == excepted   
