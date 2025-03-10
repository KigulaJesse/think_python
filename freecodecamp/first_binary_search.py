"""Find first occurence"""

def first_binary_search(array, target):
    """First occurence"""
    first = 0
    last = len(array) - 1
    result = -1

    while first <= last:
        print(first," ",last)
        midpoint = (first + last) // 2
        print(midpoint)
        if array[midpoint] == target:
            # print("[midpoint, value]:",f"[{midpoint}, {array[midpoint]}]")
            result = midpoint
            first = midpoint + 1
            # print(first)
        elif array[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint -1
    return result
#         0,1,2,3,4,5,6,7,8
array1 = [1,2,7,7,7,7,9,10,11]
RESULT1 = first_binary_search(array1, 7)
print(RESULT1)
