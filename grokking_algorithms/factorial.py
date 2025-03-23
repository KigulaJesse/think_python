"Simple factorial"

def factorial(n):
    "Simple recursive countdown"
    if n == 1:
        return 1
    return n * factorial(n-1)
# print(factorial(4))

def sum_array(arr):
    "Simple sum recursion function"
    if len(arr) <= 1:
        return arr[0]
    return arr[-1] + sum(arr[:len(arr)-1])

# print(sum_array([5,4]))

def count_numbers(arr):
    "Count numbers"
    if len(arr) <= 1:
        return 1
    return 1 + count_numbers(arr[:len(arr)-1])

def find_max(arr,index=0,largest=0):
    "Find max"
    if arr[index] > largest:
        largest = arr[index]
    if index == len(arr) -1:
        return largest
    return find_max(arr, index + 1, largest)

print(find_max([5,4,6,10,3,3]))
