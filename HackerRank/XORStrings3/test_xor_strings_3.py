import pytest

from xor_strings_3 import strings_xor


@pytest.mark.parametrize('first_str,second_str,expected', [
    ["10101", "00101", "10000"],
    ["01010", "10101", "11111"],
])
def test_strings_xor(first_str, second_str, expected):
    assert strings_xor(first_str, second_str) == expected
