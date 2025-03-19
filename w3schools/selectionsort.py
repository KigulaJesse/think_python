"Selection Sort Algorithm"

def selection_sort(array):
    size = len(array)
    for i in range(size - 1):
        lowest = i
        for j in range(i + 1, size):
            print(array[j])
            print(array[lowest])
            print(array[j] < array[lowest])
            print("")
            if array[j] < array[lowest]:
                lowest = j
        array[i], array[lowest] = array[lowest], array[i]
        break
    # return array

test_array = [10,14,11,9,8]
print(selection_sort(test_array))