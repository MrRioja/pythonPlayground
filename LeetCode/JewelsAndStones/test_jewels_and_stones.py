import pytest
from jewels_and_stones import num_jewels_in_stones


@pytest.mark.parametrize("jewels,stones,expected", [
    ("z", "ZZ", 0),
    ("aA", "aAAbbbb", 3)
])
def test_num_jewels_in_stones(jewels, stones, expected):
    assert num_jewels_in_stones(jewels, stones) == expected
