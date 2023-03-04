import pytest
from pangrams import pangrams


@pytest.mark.parametrize('value,expected', [
    ('We promptly judged antique ivory buckles for the next prize', 'pangram'),
    ('We promptly judged antique ivory buckles for the prize', 'not pangram')
])
def test_pangrams(value, expected):
    assert pangrams(value) == expected
