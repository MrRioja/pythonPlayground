import pytest
from migratory_birds import migratory_birds


@pytest.mark.parametrize('array,expected', [
    ([1, 1, 2, 2, 3], 1),
    ([1, 4, 4, 4, 5, 3], 4),
    ([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4], 3)
])
def test_migratory_birds(array, expected):
    assert migratory_birds(array) == expected
