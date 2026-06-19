import math
import pytest
from code import calculate_area


def test_calculate_area_positive():
    assert calculate_area(5) == pytest.approx(math.pi * 25)


def test_calculate_area_negative():
    assert calculate_area(-3) == 0
