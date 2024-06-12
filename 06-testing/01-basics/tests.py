from intervals import overlapping_intervals

def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
    assert overlapping_intervals ((1,1), (1,1))
    assert overlapping_intervals ((1,5), (5, 7))
    assert overlapping_intervals ((1,5), (5, 2))