import pytest
from lonely_integer import lonely_integer


@pytest.mark.parametrize("array,expected", [
    ([1, 2, 3, 4, 3, 2, 1], 4)
])
def test_lonely_integer(array, expected):
    assert lonely_integer(array) == expected
