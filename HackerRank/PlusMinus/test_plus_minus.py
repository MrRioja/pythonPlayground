import pytest
from plus_minus import plus_minus


@pytest.mark.parametrize("array,expected", [
    ([1, 1, 0, -1, -1], ("0.400000", "0.400000", "0.200000"))
])
def test_plus_minus(array, expected):
    assert plus_minus(array) == expected


@pytest.mark.parametrize("array,expected", [
    ([1, 1, 0, -1, -1], ("incorrect_value", "incorrect_value", "incorrect_value"))
])
def test_plus_minus_error(array, expected):
    assert plus_minus(array) != expected
