import pytest
from granding_students import grading_students


@pytest.mark.parametrize("grades,expected", [
    ([98, 84, 99, 29, 57, 100], [100, 85, 100, 29, 57, 100]),
    ([73, 67, 38, 33], [75, 67, 40, 33])
])
def test_grading_students(grades, expected):
    assert grading_students(grades) == expected


@pytest.mark.parametrize("grades,expected", [
    ([98, 84, 99, 29, 57, 100], [0, 0, 0, 0, 0, 0]),
    ([73, 67, 38, 33], [0, 0, 0, 0])
])
def test_grading_students_error(grades, expected):
    assert grading_students(grades) != expected
