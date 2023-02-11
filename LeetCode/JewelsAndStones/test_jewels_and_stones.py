import pytest
from jewels_and_stones import num_jewels_in_stones


@pytest.mark.parametrize("jewels,stones,expected", [
    ("z", "ZZ", 0),
    ("aA", "aAAbbbb", 3)
])
def test_num_jewels_in_stones(jewels, stones, expected):
    assert num_jewels_in_stones(jewels, stones) == expected


@pytest.mark.parametrize("jewels,stones,expected", [
    ("z", "ZZ", 1000),
    ("aA", "aAAbbbb", 1000)
])
def test_num_jewels_in_stones_error(jewels, stones, expected):
    assert num_jewels_in_stones(jewels, stones) != expected
