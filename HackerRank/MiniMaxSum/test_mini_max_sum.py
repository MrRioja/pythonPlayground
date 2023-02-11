import pytest
from mini_max_sum import mini_max_sum


@pytest.mark.parametrize("array,expected", [
    ([7, 69, 2, 221, 8974], (299, 9271))
])
def test_mini_max_sum(array, expected):
    assert mini_max_sum(array) == expected


@pytest.mark.parametrize("array,expected", [
    ([7, 69, 2, 221, 8974], (0, 0))
])
def test_mini_max_sum_test(array, expected):
    assert mini_max_sum(array) != expected
