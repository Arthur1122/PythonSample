import pytest
from calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(3, 2) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(-1, -1) == -2

def test_subtract(calculator):
    assert calculator.subtract(3, 2) == 1
    assert calculator.subtract(-1, 1) == -2
    assert calculator.subtract(-1, -1) == 0

def test_multiply(calculator):
    assert calculator.multiply(3, 2) == 6
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(-1, -1) == 1

def test_divide(calculator):
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(-1, 1) == -1
    assert calculator.divide(-1, -1) == 1
    with pytest.raises(ValueError):
        calculator.divide(1, 0)
