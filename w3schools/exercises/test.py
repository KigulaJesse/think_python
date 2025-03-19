#             0, 1, 2, 3, 4, 5, 6
test_array = [0, 1, 2, 3, 4, 5, 6]

print(test_array[:0:])
print(test_array[:1:])
print(test_array[:2:])
print(test_array[:3:])
print(test_array[:4:])
print(test_array[:5:])
print(test_array[:6:])
print(test_array[:7:])
print("")
print(len(test_array))
print(range(len(test_array)))
for i in range(len(test_array) + 1):
    print(test_array[:i:])

print("")
for i in test_array[:len(test_array):]:
    print(i)
    print(test_array[:i:])