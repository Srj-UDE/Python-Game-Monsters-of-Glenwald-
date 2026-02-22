from project import calc, ability, generate_integer
from unittest.mock import patch #(Source:https://docs.python.org/3/library/unittest.mock.html)
from inputimeout import TimeoutOccurred
import random

def test_generate_integer():
    for i in range(1,4):
        if i == 1:
            num = generate_integer(i)
            assert 100 <= num <= 999
        elif i ==2:
            num = generate_integer(i)
            assert 1000 <= num <= 9999
        elif i == 3:
            num = generate_integer(i)
            assert 10 <= num <= 999

def test_ability():
     assert ability(3) == "monh"
     assert ability(2) == "wara"
     assert ability(5) == "warh"
     assert ability(1) == "af"
     assert ability(4) == "af"

@patch('project.inputimeout', return_value = 200 )
def test_calc_value(mock_i):
        i = random.randint(10,9999)
        j = random.randint(10,9999)
        result = calc(i,j)
        assert result == [200,i+j]

@patch("project.inputimeout", side_effect =TimeoutOccurred ) #side_effect (Source:https://docs.kanaries.net/topics/Python/side-effect-in-python)
def test_calc_timeout(mock):
        i = random.randint(10,9999)
        j = random.randint(10,9999)
        result = calc(i,j)
        assert result == [-1,i+j]

@patch("project.inputimeout", side_effect = ValueError )
def test_calc_val_error(mock):
        i = random.randint(10,9999)
        j = random.randint(10,9999)
        result = calc(i,j)
        assert result == [-1,i+j]
