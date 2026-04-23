import pytest
from simple_math_new import SimpleMath


@pytest.fixture
def calc():
    return SimpleMath()


@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (5, 25),
    (-3, 9),
    (-7, 49),
    (0, 0),
])
def test_square(calc, input, expected):
    assert calc.square(input) == expected


@pytest.mark.parametrize("input,expected", [
    (2, 8),
    (4, 64),
    (-3, -27),
    (-2, -8),
    (0, 0),
])
def test_cube(calc, input, expected):
    assert calc.cube(input) == expected