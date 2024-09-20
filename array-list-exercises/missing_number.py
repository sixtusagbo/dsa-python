#!/usr/bin/env python3
"""
Missing Number
Write a function to find the missing number in a given integer array of 1 to 100. The function takes to parameter the array and the number of elements that needs to be in array.  For example if we want to find missing number from 1 to 6 the second parameter will be 6.

Example
missing_number([1, 2, 3, 4, 6], 6) # 5
"""


def missing_number(arr, n):
    """Finds the missing number"""
    # Sum of n series w/ arithmetic progression algorithm
    expected_total = n * (n + 1) // 2
    actual_total = sum(arr)
    return expected_total - actual_total


print(missing_number([1, 2, 3, 4, 6], 6))
print(missing_number([6, 2, 3, 4, 1], 6))
