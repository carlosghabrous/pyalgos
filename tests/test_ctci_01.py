import pytest

import ctci_01

s1 = ''.join(list())
s2 = ''.join(['c']*10)
s3 = ''.join(['a','z','4','q'])

@pytest.mark.parametrize('input_string,expected', [(s1, False), (s2, False), (s3, True)])
def test_unique_chars_with_struct(input_string, expected):
    assert ctci_01.unique_chars_with_structure(input_string) == expected
    assert ctci_01.unique_chars_no_structure(input_string) == expected

s1 = 'abCd  eFHG'
s2 = 'abCd eFHG '
@pytest.mark.parametrize('s1,s2,expected', [(s1, s1, False), (s1, s2, True), (s1, s1.lower(), False)])
def test_strings_permutation(s1, s2, expected):
    assert ctci_01.are_permutation(s1, s2) == expected
 
