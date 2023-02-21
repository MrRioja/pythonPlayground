import pytest
from camel_case import camel_case


@pytest.mark.parametrize("string,expected", [
    ("saveChangesInTheEditor", 5),
    ("oneTwoThree", 3),
])
def test_camel_case(string, expected):
    assert camel_case(string) == expected
