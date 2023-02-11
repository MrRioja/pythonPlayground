import pytest
from intersection_of_two_arrays import intersection


@pytest.mark.parametrize("array1,array2,expected", [
    ([4, 9, 5], [9, 4, 9, 8, 4], {4, 9}),
    ([1, 2, 2, 1], [2, 2], {2}),
])
def test_intersection(array1, array2, expected):
    assert intersection(array1, array2) == expected


@pytest.mark.parametrize("array1,array2,expected", [
    ([4, 9, 5], [9, 4, 9, 8, 4], [0]),
    ([1, 2, 2, 1], [2, 2], [0]),
])
def test_intersection_error(array1, array2, expected):
    assert intersection(array1, array2) != expected
