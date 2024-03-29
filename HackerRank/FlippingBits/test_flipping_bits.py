import pytest
from flipping_bits import flipping_bits


@pytest.mark.parametrize("number,expected", [
    (2147483647, 2147483648),
    (1, 4294967294),
    (0, 4294967295)
])
def test_flipping_bits(number, expected):
    assert flipping_bits(number) == expected
