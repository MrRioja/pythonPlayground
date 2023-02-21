import pytest
from diagonal_difference import get_diagonal_difference


@pytest.mark.parametrize("array,expected", [
    ([[11, 2, 4], [4, 5, 6], [10, 8, -12]], 15)
])
def test_get_diagonal_difference(array, expected):
    assert get_diagonal_difference(array) == expected
