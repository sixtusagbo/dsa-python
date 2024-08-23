#!/usr/bin/env python3
"""Search for an element in array"""

from constants import my_array


def linear_search(arr, target):  # O(n)
    """Search for an item in an array

    Args:
        arr: Array to be searched or haystack
        target: Item that is being searched for or needle
    """
    for i in range(len(arr)):  # O(n)
        if arr[i] == target:  # O(1)
            return i  # O(1)
    return -1  # O(1)


print(linear_search(my_array, 3))
