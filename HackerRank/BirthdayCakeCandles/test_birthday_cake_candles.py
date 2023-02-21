import pytest
from birthday_cake_candles import birth_day_cake_candles


@pytest.mark.parametrize("candles,expected", [
    ([4, 5, 1, 9, 10, 900, 30, 4, 4, 7, 4], 1),
    ([3, 2, 1, 3], 2),
])
def test_birth_day_cake_candles(candles, expected):
    assert birth_day_cake_candles(candles) == expected
