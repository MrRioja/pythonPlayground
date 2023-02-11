import pytest
from shuffle_string import restore_string


@pytest.mark.parametrize("string,indices,expected", [
    ("codeleet", [4, 5, 6, 7, 0, 2, 1, 3], "leetcode"),
    ("aaiougrt", [4, 0, 2, 6, 7, 3, 1, 5], "arigatou"),
])
def test_restore_string(string, indices, expected):
    assert restore_string(string, indices) == expected


@pytest.mark.parametrize("string,indices,expected", [
    ("codeleet", [4, 5, 6, 7, 0, 2, 1, 3], "incorrect_value"),
    ("aaiougrt", [4, 0, 2, 6, 7, 3, 1, 5], "incorrect_value"),
])
def test_restore_string_error(string, indices, expected):
    assert restore_string(string, indices) != expected
