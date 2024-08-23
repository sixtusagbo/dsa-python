#!/usr/bin/env python3
import array

my_array = array.array("i", [1, 2, 3, 4, 5])
print(my_array)
my_array.insert(100, 6)
print(my_array)


def traverse_array(array):
    for i in array:
        print(i)


traverse_array(my_array)
