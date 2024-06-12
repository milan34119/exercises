# Write your own tests for the housing.py file here.
# You must include the tests asked for in the assignment for full credit.
# You may add additional tests if you would like to test your code more thoroughly.
# Additional tests will not result in a higher grade.
# This file must be able to be run without error in order to receive credit for the required testing.
####
# Schrijf hier je eigen tests voor het housing.py bestand.
# Je moet de gevraagde tests in de opdracht opnemen voor volledige waardering.
# Je mag extra tests toevoegen als je je code grondiger wilt testen.
# Extra tests zullen niet leiden tot een hoger cijfer.
# Dit bestand moet zonder fouten uitgevoerd kunnen worden om punten te krijgen voor de vereiste testen.

from housing import *
import pytest
# @pytest.mark.parametrize('area', [
#     '5489', '9999', '7854', '4222'
# ])
# @pytest.mark.parametrize('number_of_rooms', [
#     '2', '5', '8'
# ])
# def test_maximum_occupants():
#     gebouw = Residence('Diestsesteenweg', 200, 4)
#     actual = gebouw.maximum_occupants
#     expected = 8
#     assert expected == actual
    


import pytest
from housing import *

@pytest.mark.parametrize("area, number_of_rooms, expected", [
    (30, 1, 1),
    (40, 1, 2),  
    (200, 3, 6), 
    (72, 3, 3),  
    (100, 2, 4),  
])
def test_maximum_occupants(area, number_of_rooms, expected):
    gebouw = Villa('diestsesteenweg', area, number_of_rooms, 5)
    actual = gebouw.maximum_occupants
    assert expected == actual