def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) > 0:

        maximum = ints[0]

        minimum = ints[0]
        for num in ints:

            if num > maximum:
                maximum = num

            if num < minimum:
                minimum = num

        return (minimum,maximum)

    return None

## Example Test Case of Ten Integers

print("--------------------------------------------Test 1--------------------------------------")

import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


print("--------------------------------------------Test 2--------------------------------------")

l = [1,2,3,4,5]
print(get_min_max(l))

print("--------------------------------------------Test 3--------------------------------------")

l = list()
print(get_min_max(l))

print("--------------------------------------------Test 4--------------------------------------")
l = [i for i in range(-10, 1)]  # a list containing 0 - 9
random.shuffle(l)

print(get_min_max(l))