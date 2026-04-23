from simple_math import SimpleMath
import pytest

@pytest.fixture
def calc():
    return SimpleMath()
#  для метода square
def test_square_positive(calc):
    assert calc.square(4) == 16

def test_square_negative(calc):
    assert calc.square(-4) == 16

def test_square_zero(calc):
    assert calc.square(0) == 0

#  для метода cube
def test_cube_positive(calc):
    assert calc.cube(2) == 8

def test_cube_negative(calc):
    assert calc.cube(-2) == -8

def test_cube_zero(calc):
    assert calc.cube(0) == 0