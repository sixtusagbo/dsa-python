#!/usr/bin/env python3
"""Manipulating Python lists."""

letters = ["a", "b", "c", "d", "e", "f"]

# Deleting
# letters.pop(0) # O(1) time since it's at the beginning of the list, O(1) Space # Remove the element at index 0
# letters.pop() # O(n) time, O(1) Space # Remove the last element
# letters.pop(2)  # O(n) time, O(1) Space Remove the element at index 2
# pop method returns the removed element
# print(letters.pop())
# del letters[:3]  # O(n) time, O(1) space you can delete multiple elements by slicing
# del letters[2]  # O(n) time, O(1) space Remove the element at index 2
letters.remove("b")  # O(n) time, O(1) space
print(letters)
