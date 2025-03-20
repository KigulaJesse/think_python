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