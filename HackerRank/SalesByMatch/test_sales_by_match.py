import pytest
from sales_by_match import sock_merchant


@pytest.mark.parametrize('length,array,expected', [
    (7, [1, 2, 1, 2, 1, 3, 2], 2),
    (9, [10, 20, 20, 10, 10, 30, 50, 10, 20], 3)
])
def test_(length, array, expected):
    assert sock_merchant(length, array) == expected
