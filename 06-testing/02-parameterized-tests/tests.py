import pytest
from parantheses import matching_parentheses

# @pytest.mark.parametrize("string", [
#     '',
#     '()',
#     "()()",
#     "()()()",
# ])
# def test_matching_parentheses(string):
#     actual = matching_parentheses(string)
#     assert actual == True(f"The paranthese match")
    
@pytest.mark.parametrize('string', [
    '',
    '()',
    '(())',
    '()()()',
    '(())()',
])
def test_matching_parentheses(string):
    actual = matching_parentheses(string)
    assert actual == True, f'{string} has matching parentheses'
    
    
@pytest.mark.parametrize('string', [
    '((',
    '))',
    '(]',
    '](',
])
def test_not_matching_parentheses(string):
    actual = matching_parentheses(string)
    assert actual == False, f'{string} has no matching parentheses'