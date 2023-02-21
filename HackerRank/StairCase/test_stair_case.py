import pytest
from stair_case import staircase


@pytest.mark.parametrize("n,expected", [
    (3, "  #\n ##\n###")
])
def test_staircase(n, expected):
    assert staircase(n) == expected
