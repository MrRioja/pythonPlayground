import pytest

from zig_zag_sequence import find_zig_zag_sequence


@pytest.mark.parametrize('arr,n,expected', [
    ([2, 3, 5, 1, 4], 5, "1 2 5 4 3"),
    ([1, 2, 3, 4, 5, 6, 7], 7, "1 2 3 7 6 5 4"),
    ([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 11,
     "1 2 3 4 5 11 10 9 8 7 6"),
])
def test_find_zig_zag_sequence(arr, n, expected):
    assert find_zig_zag_sequence(arr, n) == expected
