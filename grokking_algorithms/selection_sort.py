"""Selection sort algorithm"""

def find_smallest(arr):
    "Find smallest value in an array"
    smallest = arr[0]
    index = 0
    for key,value in enumerate(arr):
        if value < smallest:
            smallest = value
            index = key
    return index

def selection_sort(disordered_array):
    "Selection sort function"
    ordered_array = []
    for _ in range(len(disordered_array)):
        index2 = find_smallest(disordered_array)
        ordered_array.append(disordered_array.pop(index2))
    return ordered_array

#             0,1,2,3,4,5
test_array = [7,4,8,9,2,10]
index1 = find_smallest(test_array)

print(f"test_array[{index1}]","=",f"{test_array[index1]}")

sorted_array = selection_sort(test_array)
print(sorted_array)
