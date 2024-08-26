import numpy as np

weather_stats = np.array(
    [
        [11, 15, 10, 6],
        [10, 14, 11, 5],
        [12, 17, 12, 8],
        [15, 18, 14, 9],
    ]
)

print("before")
print(weather_stats)

# In numpy, axis 0 is the row and axis 1 is the column

"""Inserting
# moddedStats = np.insert(weather_stats, 0, [[1, 2, 3, 4]], axis=0)
moddedStats = np.append(weather_stats, [[1, 2, 3, 4]], axis=0)
print()
print(moddedStats)
"""


# The time complexity of this function is O(1)
# Space complexity is O(1) since we are not using any extra space
def access_element(array, rowIndex, colIndex):  # O(1)
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        raise ValueError("Invalid index")
    print(
        "Element at rowIndex {}, colIndex {} is {}".format(
            rowIndex, colIndex, array[rowIndex][colIndex]
        )
    )
    return array[rowIndex][colIndex]


# access_element(weather_stats, 1, 2)


# The time complexity of this function is O(m*n) where
# m is the number of rows and n is the number of columns
# But if the number of rows and columns are the same, then
# the time complexity is quadratic - O(n^2) since m = n
# Space complexity is O(1) since we are not using any extra space
def traverse_2d_array(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


# traverse_2d_array(weather_stats)


# The time complexity of this function is O(m*n)
# Space complexity is O(1) since we are not using any extra space
def search_2d_array(array, target):  # O(mn)
    for i in range(len(array)):  # O(mn)
        for j in range(len(array[0])):  # O(n)
            if array[i][j] == target:  # O(1)
                return "Element found at rowIndex {}, colIndex {}".format(i, j)

    return "Element not found"


# print(search_2d_array(weather_stats, 14))

# Time complexity of deletion from numpy array is O(m*n)
# Space complexity is O(m*n) since we are creating a new array
# new_weather_stats = np.delete(weather_stats, 0, axis=0) # Row
new_weather_stats = np.delete(weather_stats, 0, axis=1)  # Column
print(new_weather_stats)
