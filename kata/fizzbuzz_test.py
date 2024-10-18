import pytest
from kata.fizzbuzz import fizzbuzz

def test_fizzbuzz():
    assert fizzbuzz(1) == 1

def test_fizzbuzz2():
    assert fizzbuzz(2) == 2


def test_fizzbuzz3():
    assert fizzbuzz(3) == 'Fizz'

def test_fizzbuzz5():
    assert fizzbuzz(5) == 'Buzz'

def test_fizzbuzz6():
    assert fizzbuzz(6) == 'Fizz'