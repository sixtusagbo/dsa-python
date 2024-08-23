#!/usr/bin/env python3   
import array

my_array = array.array("i", [1, 2, 3, 4, 5])

print(my_array)
my_array.remove(3)  # Time - O(N), Space - O(1)
print(my_array)
