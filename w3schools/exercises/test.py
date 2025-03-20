

# def compare(a, b):
#     print(a)
#     print(b)
#     print(a, "<", b, " = ", a < b)
#     print(a, ">", b, " = ", a > b)
#     print("int(True) = ",int(True))
#     print("int(False) = ",int(False))
#     print("True - False =", True - False)
#     print("False - True =", False - True)
#     return ((a < b) - (a > b))

# compare("apple", "appld")

test_tuple = (3,4,5)

print(test_tuple[1])

# # #             0, 1, 2, 3, 4, 5, 6, 7, 8
# # test_array = [1, 7, 3, 0, 5, 4, 7, 8, 9]

# # print(test_array[:0:])
# # print(test_array[:1:])
# # print(test_array[:2:])
# # print(test_array[:3:])
# # print(test_array[:4:])
# # print(test_array[:5:])
# # print(test_array[:6:])
# # print(test_array[:7:])
# # print("")

# # print(len(test_array))
# # print(range(len(test_array)))

# # ####--- range just creates iterators over a range, so it allows us to go beyond the array size
# # for i in range(len(test_array) + 1):
# #     # print(i)
# #     print(test_array[:i:])

# # print("")

# # ####--- array slicing stops exactly at the last index even if you add +1. 
# # # Since the last index is exclusive, it will not print the last item
# # for i,_ in enumerate(test_array[:len(test_array)+1:]):
# #     # print(i)
# #     print(test_array[:i:])
# # print(test_array[:i+1:])

# # print("")
# # print(test_array[:len(test_array):])
# # print(test_array[:len(test_array)+1:])


# #              0,1,2,3,4,5
# other_array = [5,3,9,2,8,7]
# # print(other_array[5:])
# # print(other_array[4:])
# # print(other_array[3:])
# # print(other_array[2:])
# # print(other_array[1:])
# # print(other_array[0:])

# size = len(other_array)

# print(range(size))

# for j in range(size):
#     print(j," : ",other_array[j])

# print("")

# for j in range(size-1, -1, -1):
#     print(j," : ",other_array[j])
    

# "Bubble Sort Exercises from ChatGPT"

# def basic_bubblesort(array):
#     "This Bubble Sort Function organises array in Ascending Order"
#     size = len(array)
#     # print(range(size-1))
#     for i,_ in enumerate(array[:size:]):
#         for j,_ in enumerate(array[:size-i-1:]):
#             print(array[:size-i:])
#             print(j)
#             print(j + 1)
#             print("")
#             if array[j] > array[j+1]:
#                 array[j],array[j+1] = array[j+1],array[j]
#     return array

# # test_array = [5, 3, 8, 4, 2]
# # print(basic_bubblesort(test_array))

# # def descending_bubble(array):
# #     "This is descending order Bubble Sort"
# #     size = len(array)
# #     for i in range(size-1):
# #         for j in range(size-i-1):
# #             if array[j] < array[j+1]:
# #                 array[j],array[j+1] = array[j+1],array[j]
# #     return array

# # test_array = [5, 3, 8, 4, 2]
# # print(descending_bubble(test_array))

# def descending_bubble_alternate(array):
#     "This is descending order Bubble Sort"
#     size = len(array)
#     for i in range(size-1):
#         for j in range(size-1, i, -1):
#             print(j, size-i-1)
#             print(array[j],">" ,array[j-1]," = ", array[j] > array[j-1] ,"(",j,j-1,")")
#             if array[j] > array[j-1]:
#                 array[j], array[j-1] = array[j-1], array[j]
#         # print(array)
#         print("")
#     return array

# test_array = [5, 3, 8, 4, 2]
# print(descending_bubble_alternate(test_array))

# def descending_bubble_sort_count_swaps(array):
#     size = len(array)
#     swaps = 0
#     for i in range(size-1):
#         for j in range(size-1, i, -1):
#             print(j, size-i-1)
#             print(array[j],">" ,array[j-1]," = ", array[j] > array[j-1] ,"(",j,j-1,")")
#             if array[j] < array[j-1]:
#                 swaps += 1
#                 array[j], array[j-1] = array[j-1], array[j]
#         # print(array)
#         print("")
#     return array,swaps

# test_array = [5, 3, 8, 4, 2]
# print(descending_bubble_sort_count_swaps(test_array))








# # def descending_bubble_alternate(array):
# #     "This is descending order Bubble Sort"
# #     size = len(array)
# #     for i in range(size-1):
# #         print(i)
# #         for j in range(i, size-1, 1):
# #             print(j)
# #         #     print(array[j],">" ,array[j-1]," = ", array[j] > array[j-1] ,"(",j,j-1,")")
# #         #     if array[j] > array[j-1]:
# #         #         array[j], array[j-1] = array[j-1], array[j]
# #         # print(array)
# #         # print("")
# #     # return array

# # test_array = [5, 3, 8, 4, 2]
# # print(descending_bubble_alternate(test_array))


# # def descending_bubble(array):
# #     "This is descending order Bubble Sort"
# #     size = len(array)
# #     for i in range(size-1):
# #         for j in range(size-i-1):
# #             print(j)
# #             # if array[j] < array[j+1]:
# #             #     array[j],array[j+1] = array[j+1],array[j]
# #         print("")
# #     return array

# # test_array = [5, 3, 8, 4, 2]
# # print(descending_bubble(test_array))
# # print("================")
