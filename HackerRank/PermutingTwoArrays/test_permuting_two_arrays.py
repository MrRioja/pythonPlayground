import pytest

from permuting_two_arrays import two_arrays


@pytest.mark.parametrize('k,a,b,expected', [
    (10, [2, 1, 3], [7, 8, 9], 'YES'),
    (5, [1, 2, 2, 1], [3, 3, 3, 4], 'NO'),
    (10, [7, 6, 8, 4, 2], [5, 2, 6, 3, 1], 'NO')
])
def test_two_arrays(k, a, b, expected):
    assert two_arrays(k, a, b) == expected
