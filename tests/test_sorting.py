from _pytest.monkeypatch import K
import pytest

import sorting
from random import randint

arr1 = list(i for i in range(10, 0, -1))
arr2 = [1] * 10
arr3 = [randint(0,50) for i in range(10)]
arr4 = list(i for i in range(0,10))

@pytest.mark.parametrize(('input_arr, expected_arr'), 
                            [(arr1, sorted(arr1)), 
                            (arr2, sorted(arr2)), 
                            (arr3, sorted(arr3)), 
                            (arr4, sorted(arr4))])
def test_bubble_sort(input_arr, expected_arr):
    sorting.bubble_sort(input_arr)
    assert input_arr == expected_arr

@pytest.mark.parametrize(('input_arr, expected_arr'), 
                            [(arr1, sorted(arr1)), 
                            (arr2, sorted(arr2)), 
                            (arr3, sorted(arr3)), 
                            (arr4, sorted(arr4))])
def test_selection_sort(input_arr, expected_arr):
    sorting.selection_sort(input_arr)
    assert input_arr == expected_arr

@pytest.mark.parametrize(('input_arr, expected_arr'), 
                            [(arr1, sorted(arr1)), 
                            (arr2, sorted(arr2)), 
                            (arr3, sorted(arr3)), 
                            (arr4, sorted(arr4))])
def test_merge_sort(input_arr, expected_arr):
    assert sorting.merge_sort(input_arr) == expected_arr


@pytest.mark.parametrize(('input_arr, expected_arr'), 
                            [(arr1, sorted(arr1)), 
                            (arr2, sorted(arr2)), 
                            (arr3, sorted(arr3)), 
                            (arr4, sorted(arr4))])
def test_quick_sort(input_arr, expected_arr):
    sorting.quick_sort(input_arr)
    assert input_arr == expected_arr


# @pytest.mark.parametrize(('input_arr, expected_arr'), 
#                             [(arr1, sorted(arr1)), 
#                             (arr2, sorted(arr2)), 
#                             (arr3, sorted(arr3)), 
#                             (arr4, sorted(arr4))])
# def test_radix_sort(input_arr, expected_arr):
#     assert sorting.radix_sort(input_arr) == expected_arr

@pytest.mark.parametrize(('input_arr, expected_arr'), 
                            [(arr1, sorted(arr1)), 
                            (arr2, sorted(arr2)), 
                            (arr3, sorted(arr3)), 
                            (arr4, sorted(arr4))])
def test_counting_sort(input_arr, expected_arr):
    assert sorting.counting_sort(input_arr) == expected_arr


@pytest.mark.parametrize(('input_arr, k'),
                            [(arr1, randint(1, len(arr1))), 
                            (arr3, randint(1, len(arr3))),
                            (arr4, randint(1, len(arr4)))])
def test_kth_element(input_arr, k):
    assert sorting.kth_element(input_arr, k) == sorted(input_arr)[k-1]