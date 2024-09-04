#!/usr/bin/env python3

numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.insert(0, 8)  # Time complexity: O(n), Space complexity: O(1)
numbers.append(13)  # Time complexity: O(1), Space complexity: O(1)
odd_numbers = [7, 9, 11]  # Time complexity: O(n), Space complexity: O(n)
numbers.extend(odd_numbers)
print(numbers)
