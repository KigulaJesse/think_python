"Bubble Sort Exercises from ChatGPT"

def basic_bubblesort(array):
    "This Bubble Sort Function organises array in Ascending Order"
    size = len(array)
    # print(range(size-1))
    for i,_ in enumerate(array[:size:]):
        for j,_ in enumerate(array[:size-i-1:]):
            print(array[:size-i:])
            print(j)
            print(j + 1)
            print("")
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

test_array = [5, 3, 8, 4, 2]
print(basic_bubblesort(test_array))

# def descending_bubble(array):
#     "This is descending order Bubble Sort"
#     size = len(array)
#     for i in range(size-1):
#         for j in range(size-i-1):
#             if array[j] < array[j+1]:
#                 array[j],array[j+1] = array[j+1],array[j]
#     return array

# # test_array = [5, 3, 8, 4, 2]
# # print(descending_bubble(test_array))

# def descending_bubble_alternate(array):
#     "This is descending order Bubble Sort"
#     size = len(array)
#     for i in range(size-1):
#         print(i)
#         print(array[:i:])
#         print(array[i::])
#         print("")
#         # for j in array[:i:-1]:
#         #     # print(j)
#         #     print(i)
#         #     print(array[:i:-1])
#         # print("")   
#     return array

# test_array = [5, 3, 8, 4, 2]
# print(descending_bubble_alternate(test_array))