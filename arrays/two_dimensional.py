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

"""Inserting
# moddedStats = np.insert(weather_stats, 0, [[1, 2, 3, 4]], axis=0)
moddedStats = np.append(weather_stats, [[1, 2, 3, 4]], axis=0)
print()
print(moddedStats)
"""


def access_element(array, rowIndex, colIndex):  # O(1)
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        raise ValueError("Invalid index")
    print(
        "Element at rowIndex {}, colIndex {} is {}".format(
            rowIndex, colIndex, array[rowIndex][colIndex]
        )
    )
    return array[rowIndex][colIndex]


access_element(weather_stats, 1, 2)
