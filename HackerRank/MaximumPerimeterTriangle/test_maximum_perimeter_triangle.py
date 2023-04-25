import pytest

from maximum_perimeter_triangle import maximum_perimeter_triangle


@pytest.mark.parametrize('sticks,expected', [
    ([1, 2, 3], [-1]),
    ([1, 1, 1, 3, 3], [1, 3, 3]),
    ([1, 1, 1, 2, 3, 5], [1, 1, 1]),
])
def test_maximum_perimeter_triangle(sticks, expected):
    assert maximum_perimeter_triangle(sticks) == expected
