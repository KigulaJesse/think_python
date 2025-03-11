"""Chapter 1"""

def binary_search(array, target):
    "Binary Search"
    first = 0
    last = len(array) - 1

    while first <= last:
        middle = (first + last) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            first = middle + 1
        else:
            last = middle - 1
    return None
#         0,1,2,3,4,5
array1 = [1,2,4,6,7,9]
print(binary_search(array1, 4))

