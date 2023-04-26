import pytest

from drawing_book import page_count


@pytest.mark.parametrize('n,p,expected', [
    (6, 2, 1),
    (5, 4, 0),
    (6, 5, 1),
])
def test_page_count(n, p, expected):
    assert page_count(n, p) == expected
