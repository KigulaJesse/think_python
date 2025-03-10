"""Basic Binary Search from memory"""


def binary_search(array, target):
    """Basic binary search"""
    left = 0
    right = len(array) - 1

    while left <= right:
        midpoint = (left + right) // 2
        if array[midpoint] == target:
            return midpoint
        elif array[midpoint] < target:
            left = midpoint + 1
        else:
            right = midpoint - 1
    return -1

array1 = [1,2,3,4,7,7,7,8,9]
result = binary_search(array1, 4)
print(result)

