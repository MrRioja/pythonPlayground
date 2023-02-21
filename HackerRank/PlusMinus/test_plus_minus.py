import pytest
from plus_minus import plus_minus


@pytest.mark.parametrize("array,expected", [
    ([1, 1, 0, -1, -1], ("0.400000", "0.400000", "0.200000"))
])
def test_plus_minus(array, expected):
    assert plus_minus(array) == expected
