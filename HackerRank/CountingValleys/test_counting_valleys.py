import pytest
from counting_valleys import counting_valleys


@pytest.mark.parametrize("steps,path,expected", [
    [0, ["U", "D", "D", "D", "U", "D", "U", "U"], 1],
    [0, ['D', 'D', 'U', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'D'], 2]
])
def test_counting_valleys(steps, path, expected):
    assert counting_valleys(steps, path) == expected
