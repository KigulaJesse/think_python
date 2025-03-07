"""Recursive Implementation of Binary Search"""

def recursive_binary_search(array, target):
    """Recursion an important concept"""
    if len(array) == 0:
        return False

    midpoint = len(array) // 2
    if array[midpoint] == target:
        return True
    if array[midpoint] < target:
        return recursive_binary_search(array[midpoint+1:], target)
    return recursive_binary_search(array[:midpoint], target)

def verify(result):
    """
    Verifies what's found
    """
    print("Target found: ", result)

numbers = [x for x in range(1,9)]

result1 = recursive_binary_search(numbers, 12)
verify(result1)

result2 = recursive_binary_search(numbers, 6)
verify(result2)
