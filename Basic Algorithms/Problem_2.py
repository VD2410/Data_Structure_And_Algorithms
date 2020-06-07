def binarySearch(input_list, number, start, end):
    if start>end:
        return -1

    index = (start+end)//2

    if input_list[index] == number:
        return index

    left_index = binarySearch(input_list,number,start,index-1)
    right_index = binarySearch(input_list,number,index+1,end)

    if left_index > right_index:
        return left_index

    else: 
        return right_index

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1

    """

    return binarySearch(input_list, number, 0, len(input_list)-1)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")
print("--------------------------------------------Test 1--------------------------------------")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
print("--------------------------------------------Test 2--------------------------------------")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
print("--------------------------------------------Test 3--------------------------------------")
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
print("--------------------------------------------Test 4--------------------------------------")
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
print("--------------------------------------------Test 5--------------------------------------")
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

print("--------------------------------------------Test 6--------------------------------------")
test_function([[], 10])

print("--------------------------------------------Test 7--------------------------------------")
test_function([[6], -1])


