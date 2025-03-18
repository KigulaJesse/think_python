"DSA Find Lowest"

def find_lowest(array)-> list[int]:
    "Loop through array find the lowest number"
    lowest = 1000000
    index = None
    for key,value in enumerate(array):
        if value < lowest:
            lowest = value
            index = key

    return [index,lowest]

test_array = [1,78,98,-1,0]
print(find_lowest(test_array))