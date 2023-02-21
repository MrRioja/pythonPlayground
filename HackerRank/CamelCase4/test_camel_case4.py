import pytest
from camel_case4 import camel_case


@pytest.mark.parametrize("word,expected", [
    ("S;M;plasticCup()", "plastic cup"),
    ("C;V;mobile phone", "mobilePhone"),
    ("C;C;coffee machine", "CoffeeMachine"),
    ("S;C;LargeSoftwareBook", "large software book"),
    ("C;M;white sheet of paper", "whiteSheetOfPaper()"),
    ("S;V;pictureFrame", "picture frame"),
])
def test_camel_case(word, expected):
    assert camel_case(word) == expected
