import pytest
from sparse_arrays import matching_strings


@pytest.mark.parametrize("string,queries,expected", [
    (
        ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn'],
        ['13', 'abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 'sdaklfj',
            'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf', '5'],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    ),
    (['ab', 'ab', 'abc'], ['ab', 'abc', 'bc'], [2, 1, 0])
])
def test_matching_strings(string, queries, expected):
    assert matching_strings(string, queries) == expected


@pytest.mark.parametrize("string,queries,expected", [
    (
        ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn'],
        ['13', 'abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 'sdaklfj',
            'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf', '5'],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ),
    (['ab', 'ab', 'abc'], ['ab', 'abc', 'bc'], [0, 0, 0])
])
def test_matching_strings_error(string, queries, expected):
    assert matching_strings(string, queries) != expected
