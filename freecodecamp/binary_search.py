"""Implementation of Binary Search"""

def binary_search(array, target):
    """
    Returns the index of the target, else None
    """
    first = 0
    last = len(array) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if array[midpoint] == target:
            return midpoint
        elif array[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    """
    Verifies what's found
    """
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")

numbers = [x for x in range(1,11)]
print(numbers)
result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)
