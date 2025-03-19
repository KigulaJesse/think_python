"Bubble Sort Algorithm"

def bubblesort(array):
    size = len(array)
    for i in range(size -1):
        for j in range(size-i-1):
            print("i:",i)
            print("j:",j)
            print("array[j]: ",array[j])
            print("array[j+1]:",array[j+1])
            print(array)
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
            print(array)    
            print("")

    return array


def bubblesortimproved(array):
    size = len(array)
    for i in range(size -1):
        swapped = False
        for j in range(size-i-1):
            print("i:",i)
            print("j:",j)
            print("array[j]: ",array[j])
            print("array[j+1]:",array[j+1])
            print(array)
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
                swapped = True
            print(array)    
            print("")
        if swapped == False:
            break
    return array

test_array = [7,14,11,8,9]
print(bubblesort(test_array))

# my_array = [7, 3, 9, 12, 11]
# print(bubblesortimproved(my_array))






