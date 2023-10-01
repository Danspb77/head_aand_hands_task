
import random


def create_arrays(n):
    # this  main array will contain little arrays
    main_arr = []

    # generate lens of little arrays
    numbers = list(range(1, n+1))
    random.shuffle(numbers)

    # generate n little arrays
    for i in range(n):
        m = []
        # choose len of little array
        little_arr_len = numbers[i]

        # fill little array
        for j in range(1, little_arr_len+1):
            a = random.uniform(1, 10)
            m.append(a)
        main_arr.append(m)
    main_arr = sort_arrays(main_arr)
    return main_arr


# funtion to sort arrays which are included in the main array
def sort_arrays(main_arr):
    # sort even elements
    for element in range(0, len(main_arr), 2):
        main_arr[element] = merge_sort(main_arr[element])
    # sort odd elements
    for element in range(1, len(main_arr), 2):
        main_arr[element] = merge_sort(main_arr[element])
        # turn over array
        main_arr[element] = main_arr[element][::-1]

    return main_arr


def merge_sort(arr):
    # if arr consists of 1 element, it means it has already sorted

    if len(arr) <= 1:
        return arr

    # devide array on halfs
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # sort halfs with  help of recursion
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # merge sorted halfs
    return merge_arrays(left_sorted, right_sorted)


def merge_arrays(left, right):
    merge_array = []
    # find left and right borders
    l = len(left)
    r = len(right)
    i = 0
    j = 0
    # merge to little elements go firstly
    while i < l and j < r:
        if left[i] <= right[j]:
            merge_array.append(left[i])
            i += 1
        else:
            merge_array.append(right[j])
            j += 1
    # check if arrays haven't equal length
    while i < l:
        merge_array.append(left[i])
        i += 1
    while j < r:
        merge_array.append(right[j])
        j += 1
    return merge_array


