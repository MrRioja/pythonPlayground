import pytest

from subarray_division2 import birthday


@pytest.mark.parametrize('arr,d,m,expected', [
    ([4], 4, 1, 1),
    ([1, 2, 1, 3, 2], 3, 2, 2),
    ([1, 1, 1, 1, 1, 1], 3, 2, 0),
])
def test_birthday(arr, d, m, expected):
    assert birthday(arr, d, m) == expected
