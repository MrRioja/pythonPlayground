import pytest
from time_conversion import time_conversion


@pytest.mark.parametrize("time,expected", [
    ("07:05:45PM", "19:05:45"),
    ("12:37:58AM", "00:37:58"),
    ("08:37:58PM", "20:37:58"),
    ("07:45:18AM", "07:45:18"),
    ("12:45:18PM", "12:45:18"),
])
def test_time_conversion(time, expected):
    assert time_conversion(time) == expected
