"""Linear Search"""

def linear_search(array, target):
    """
    Returns the index position of target if found, else returns None
    """
    for index, value in enumerate(array):
        if value == target:
            return index
    return None

def verify(index):
    """
    Verifies what's found
    """
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print("Target not found in list")

numbers = [x for x in range(1,11)]
print(numbers)
result = linear_search(numbers, 12)
verify(result)
