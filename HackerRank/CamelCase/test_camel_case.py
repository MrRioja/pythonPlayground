import pytest
from camel_case import camel_case


@pytest.mark.parametrize("string,expected", [
    ("saveChangesInTheEditor", 5),
    ("oneTwoThree", 3),
])
def test_camel_case(string, expected):
    assert camel_case(string) == expected


@pytest.mark.parametrize("string,expected", [
    ("saveChangesInTheEditor", 0),
    ("oneTwoThree", 0),
])
def test_camel_case_error(string, expected):
    assert camel_case(string) != expected
