#!/usr/bin/env python3
"""Slice operator usage in Python lists."""

letters = ["a", "b", "c", "d", "e", "f"]

# print(letters[0:2])
# print(letters[:3])
# print(letters[2:])
# print(letters[:])

# Update multiple elements in a list
letters[:3] = ["x", "y", "z"]
print(letters)
