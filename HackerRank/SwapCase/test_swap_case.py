import pytest
from swap_case import swap_case


@pytest.mark.parametrize("string,expected", [
    ("WwW.TeStE.cOm", "wWw.tEsTe.CoM")
])
def test_swap_case(string, expected):
    assert swap_case(string) == expected
