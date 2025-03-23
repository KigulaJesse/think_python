"Bubble Sort in all forms"

def bubble_right_descending(array):
    "Bubbles to the right arranges in descending order using range"
    size = len(array)
    for i in range(size-1):
        for j in range(size-i-1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
    return array
test_array = [5, 3, 8, 4, 2]
print("Bubble Right Descending: ",bubble_right_descending(test_array))

def bubble_right_ascending(array):
    "Bubbles to the right arranges in ascending order using range"
    size = len(array)
    for i in range(size-1):
        for j in range(size-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] =  array[j+1],array[j]
    return array
test_array = [5, 3, 8, 4, 2]
print("Bubble Right Ascending: ",bubble_right_ascending(test_array))

def bubble_left_descending(array):
    "Bubbles to the left arranges in descending order using range"
    size = len(array)
    for i in range(size-1):
        for j in range(size-1, i,-1):
            if array[j] > array[j-1]:
                array[j],array[j-1] =  array[j-1],array[j]
    return array

test_array = [5, 3, 8, 4, 2]
print("Bubble Left Descending: ", bubble_left_descending(test_array))

def bubble_left_ascending(array):
    "Bubbles to the left arranges in ascending order using range"
    size = len(array)
    for i in range(size-1):
        for j in range(size-1, i, -1):
            if array[j] < array[j-1]:
                array[j],array[j-1] =  array[j-1],array[j]
    return array

test_array = [5, 3, 8, 4, 2]
print("Bubble Left Ascending:",bubble_left_ascending(test_array))

def count_swaps_bubble_sort(array):
    "Count swaps in Bubble Sort"
    size = len(array)
    swaps = 0
    for i in range(size-1):
        for j in range(size-1,i,-1):
            if array[j] < array[j-1]:
                swaps += 1
                array[j], array[j-1] = array[j-1],array[j]
    return array,swaps

test_array = [5, 3, 8, 4, 2]
print("Count Swaps Bubble Sort: ", "array,swaps = ", count_swaps_bubble_sort(test_array))  

def optimized_bubble(array):
    size = len(array)
    swaps = 0
    for i in range(size-1):
        swapped = False
        for j in range(size-1,i,-1):
            if array[j] < array[j-1]:
                swapped = True
                swaps += 1
                array[j], array[j-1] =  array[j-1], array[j]
        if not swapped: 
            "Since there are no swaps, list is sorted no need to continue"
            break
    return array,swaps

test_array = [1, 2, 3, 4, 5]
print("Count Swaps Bubble Sort: ", "array,swaps = ", optimized_bubble(test_array))

def bubble_sort_on_strings(array):
    """Bubble sort on strings"""
    size = len(array)
    for i in range(size-1):
        for j in range(size-1,i,-1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1],array[j]
    return array

test_array = ["apple", "appld", "app"]
print(bubble_sort_on_strings(test_array))

def bubblesortbycustom(array):
    """Bubble sort based on key"""
    size = len(array)
    for i in range(size-1):
        for j in range(size-i-1):
            "access second element in tuple"
            if array[j][1] < array[j+1][1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

test_tuple_array = [("a", 3), ("b", 1), ("c", 2)]
print("==========================")
print(bubblesortbycustom(test_tuple_array))