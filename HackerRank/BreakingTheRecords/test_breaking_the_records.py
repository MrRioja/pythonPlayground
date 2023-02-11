import pytest
from breaking_the_records import breaking_records


@pytest.mark.parametrize("scores,expected", [
    ([12, 24, 10, 24], (1, 1)),
    ([3, 4, 21, 36, 10, 28, 35, 5, 24, 42], (4, 0))
])
def test_breaking_records(scores, expected):
    assert breaking_records(scores) == expected


@pytest.mark.parametrize("scores,expected", [
    ([12, 24, 10, 24], ()),
    ([3, 4, 21, 36, 10, 28, 35, 5, 24, 42], ())
])
def test_breaking_records_test(scores, expected):
    assert breaking_records(scores) != expected
