from random import randint

def bubble_sort(arr):
    n = len(arr)

    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selection_sort(arr):
    n = len(arr)

    for i in range(0, n-1):
        min_j, min_arr = i, arr[i]
        
        for j in range(i, n):
            if arr[j] < min_arr:
                min_arr, min_j = arr[j], j

        arr[i], arr[min_j] = arr[min_j], arr[i]


def merge(low_half, high_half):
    if len(low_half) == 0:
        return high_half

    if len(high_half) == 0:
        return low_half

    if low_half[0] < high_half[0]:
        return low_half[0:1] + merge(low_half[1:], high_half)

    else:
        return high_half[0:1] + merge(low_half, high_half[1:])

def merge_sort(arr):
    n = len(arr)
    if n > 1:
        return merge(merge_sort(arr[0:n//2]), merge_sort(arr[n//2:]))

    else:
        return arr 


def pick_pivot(arr, low, high):
    return arr[randint(low, high)]

def partition(arr, low, high):
    pivot = pick_pivot(arr, low, high)
    start, end, i = low, high, low     

    while i <= end:
        if arr[i] < pivot:
            arr[i], arr[start] = arr[start], arr[i]
            start += 1
            i += 1

        elif arr[i] > pivot:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1

        else:
            i += 1

    return start


def quick_sort_rec(arr, low, high):
    if len(arr) == 1:
        return arr 

    if low < high:
        partition_idx = partition(arr, low, high)
        quick_sort_rec(arr, low, partition_idx-1)
        quick_sort_rec(arr, partition_idx+1, high)

def quick_sort(arr):
    quick_sort_rec(arr, 0, len(arr)-1)


def radix_sort(arr):
    pass

def counting_sort(arr):
    if not arr:
        return list()

    output_arr = [0] * len(arr)
    max_input = max(arr)

    counting_arr = [0] * (max_input + 1)
    
    for element in arr:
        counting_arr[element] += 1

    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i-1]

    for _, element in enumerate(arr):
        output_arr[counting_arr[element] - 1] = element
        counting_arr[element] -= 1

    return output_arr


### SEARCHING ###

def partition_array(arr):
    i, start, end = 0, 0, len(arr)-1
    pivot = arr[randint(0, end)]

    while i <= end:
        if arr[i] < pivot:
            arr[i], arr[start] = arr[start], arr[i]
            start += 1
            i += 1

        elif arr[i] > pivot:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1

        else:
            i += 1

    return start, end-start+1, len(arr)-1-end

def kth_element(arr, k):
    if len(arr) == 1:
        return arr[0]

    size_smaller, size_equal, size_bigger = partition_array(arr)
    if k <= size_smaller:
        return kth_element(arr[:size_smaller], k)

    elif k > size_smaller and k <= size_smaller + size_equal:
        return kth_element(arr[size_smaller:size_equal+1], k-size_smaller)

    else:
        return kth_element(arr[size_smaller+size_equal:], k-size_smaller-size_equal)





