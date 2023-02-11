import pytest
from number_line_jumps import kangaroo


@pytest.mark.parametrize("x1,v1,x2,v2,expected", [
    (4523, 8092, 9419, 8076, "YES"),
    (0, 2, 5, 3, "NO"),
])
def test_kangaroo(x1, v1, x2, v2, expected):
    assert kangaroo(x1, v1, x2, v2) == expected


@pytest.mark.parametrize("x1,v1,x2,v2,expected", [
    (4523, 8092, 9419, 8076, "NO"),
    (0, 2, 5, 3, "YES"),
])
def test_kangaroo_error(x1, v1, x2, v2, expected):
    assert kangaroo(x1, v1, x2, v2) != expected
