#!/usr/bin/env python3
# import array

# my_array = array.array("i", [1, 2, 3, 4, 5])
# print(my_array)
# my_array.insert(100, 6)
# print(my_array)


def traverse_array(arr):  # Combining all -> O(n)
    for i in arr:  # -> O(n)
        print(i)  # -> O(1)


# traverse_array(my_array)


def access_element(arr, index):  # Combined -> O(1)
    if index >= len(arr):  # O(1)
        print("Invalid index")  #  O(1)
    else:
        print(index)  # O(1)
