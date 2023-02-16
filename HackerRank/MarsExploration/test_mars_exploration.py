import pytest
from mars_exploration import mars_exploration


@pytest.mark.parametrize("message_received,message_expected", [
    ("SOSTOT", 2),
    ("SOSSPSSQSSOR", 3),
    ("SOSSOSSOS", 0),
    ("SOSSPSSQSSOR", 3),
    ("SOSOSOSOSDSDSKWOSDOSDOASDOASDFAFJDFDOSOSOWNSOSOSNDSKDDOSOSOSJDSDSOOSOSDSDOSASSOASDSAOSOSODSDSOASDWS", 67)
])
def test_mars_exploration(message_received, message_expected):
    assert mars_exploration(message_received) == message_expected
