import pytest
from search import linear_search, binary_search
from student import Student

@pytest.mark.parametrize('student_id', [
    [Student(id) for id in range(0, 100)],
    [],
    [Student(id) for id in [4, 5, 6, 11, 15, 16, 17, 18, 25, 27, 55, 56, 59, 70]]
])
@pytest.mark.parametrize('target_id', range(0, 100))
def test_search(student_id, target_id):
    expected = linear_search(student_id, target_id)
    actual = binary_search(student_id, target_id)
    assert expected is actual

#is kijkt of het dezelfde student objecten zijn (die verwijzen naar zelfde plek in het geheugen), terwijl == gewoon kijkt of de student ids overeenkomen