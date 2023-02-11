import pytest
from divisible_sum_pairs import divisible_sum_pairs


@pytest.mark.parametrize("total_numbers,divisor,array,expected", [
    (6, 3, [1, 3, 2, 6, 1, 2], 5)
])
def test_divisible_sum_pairs(total_numbers, divisor, array, expected):
    assert divisible_sum_pairs(total_numbers, divisor, array) == expected


@pytest.mark.parametrize("total_numbers,divisor,array,expected", [
    (6, 3, [1, 3, 2, 6, 1, 2], 0)
])
def test_divisible_sum_pairs_error(total_numbers, divisor, array, expected):
    assert divisible_sum_pairs(total_numbers, divisor, array) != expected
