from list_comprehensions import list_comprehensions


def test_list_comprehensions_case1(monkeypatch):
    inputs = ['1', '1', '1', '2']
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    expected_output = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    assert list_comprehensions() == expected_output


def test_list_comprehensions_case2(monkeypatch):
    inputs = ['2', '2', '2', '2']
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    expected_output = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [
        1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

    assert list_comprehensions() == expected_output
