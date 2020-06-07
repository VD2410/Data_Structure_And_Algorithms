def mergesort(input_list):

    if len(input_list) <= 1:
        return input_list

    index = len(input_list) // 2

    first = input_list[:index]
    second = input_list[index:]



    first_merged = mergesort(first)
    second_merged = mergesort(second)

    id1 = 0
    id2 = 0

    sorted_input = list()

    while id1<len(first_merged) and id2 < len(second_merged):

        if first_merged[id1] > second_merged[id2]:
            sorted_input.append(first_merged[id1])
            id1+=1

        else:
            sorted_input.append(second_merged[id2])
            id2+=1

    if id1<len(first_merged):

        sorted_input += first_merged[id1:]

    if id2 <len(second_merged):
        sorted_input += second_merged[id2:]


    return sorted_input
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    sorted_input = mergesort(input_list)

    i=0
    num1 = 0
    num2 = 0

    while i<len(sorted_input):

        if i%2 == 0:
            num1 = num1*10 + sorted_input[i]

        else:

            num2 = num2*10 + sorted_input[i]

        i += 1


    rearrange = list([num1,num2])

    return rearrange

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

print("--------------------------------------------Test 1--------------------------------------")

test_function([[1, 2, 3, 4, 5], [542, 31]])

print("--------------------------------------------Test 2--------------------------------------")

test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

print("--------------------------------------------Test 3--------------------------------------")

test_function([[], []])

print("--------------------------------------------Test 4--------------------------------------")

test_function([[1], [1]])

print("--------------------------------------------Test 5--------------------------------------")

test_function([[-1,-1], [-1, -1]])

print("--------------------------------------------Test 6--------------------------------------")

test_function([[1,1,1], [11, 1]])