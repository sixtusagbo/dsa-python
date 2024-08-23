#!/usr/bin/env python3

import array
import numpy as np

#  Empty array creation Time Complexity: O(1) | Space Complexity: O(1)
my_array = array.array("i")
print(my_array)
# Array creation with elements Time Complexity: O(n) | Space Complexity: O(n)
my_array1 = array.array("i", [1, 2, 3, 4, 5])
print(my_array1)

# Empty array creation Time Complexity: O(1) | Space Complexity: O(1)
np_array = np.array([], dtype=int)
print(np_array)
# Array creation with elements Time Complexity: O(n) | Space Complexity: O(n)
np_array1 = np.array([1, 2, 3, 4, 5])
print(np_array1)
