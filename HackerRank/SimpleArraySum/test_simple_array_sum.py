import pytest
from simple_array_sum import sum_array_elements


@pytest.mark.parametrize("vector,expected", [
    ([338, 65, 713, 595, 428, 610, 728, 573, 871, 868], 5789)
])
def test_sum_array_elements(vector, expected):
    assert sum_array_elements(vector) == expected
