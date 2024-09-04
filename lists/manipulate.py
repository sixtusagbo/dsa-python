#!/usr/bin/env python3
"""Manipulating Python lists"""

letters = ["a", "b", "c", "d", "e", "f"]

# Deleting
# letters.pop(0) # O(1) time since it's at the beginning of the list, O(1) Space # Remove the element at index 0
# letters.pop() # O(n) time, O(1) Space # Remove the last element
# letters.pop(2)  # O(n) time, O(1) Space Remove the element at index 2
# pop method returns the removed element
# print(letters.pop())
# del letters[:3]  # O(n) time, O(1) space you can delete multiple elements by slicing
# del letters[2]  # O(n) time, O(1) space Remove the element at index 2
# letters.remove("b")  # O(n) time, O(1) space
# print(letters)

# Searching for an element in a list
# in operator
"""
target = "c"
if target in letters:  # O(n) time, O(1) space
    print(f"{target} found in the list")
else:
    print(f"{target} not found in the list")
"""


"""
# index method
def find_element(lst, target):  # O(n) time, O(1) space
    for index, element in enumerate(lst):
        if element == target:
            return index
    return -1


# print(find_element(letters, "z"))
print(find_element(letters, "e"))
"""

# List operations/functions
# + operator
"""
a = [1, 2, 3]
b = [4, 5, 6, 7]
c = a + b
print(c)
"""

# * operator
"""
a = [0, 1]
a = a * 4
print(a)
"""

# len function
"""
a = [1, 2, 3, 4, 5]
print(len(a))
"""

# min and max functions
"""
a = [1, 2, 3, 4, 5]
print(min(a))
print(max(a))
"""

# sum function
"""
a = [2, 4, 10]
print(sum(a))
# We can combine to get the average
print(sum(a) / len(a))
"""

# lists and strings
# Converting strings to list
a = "hello world from Nigeria"
# b = list(a)
# print(b) # ['h', 'e', 'l', 'l', 'o']
b = a.split()
print(b)
phone = "123-456-789"
c = phone.split("-")
print(c)
# Converting list to string
print("-".join(c))
