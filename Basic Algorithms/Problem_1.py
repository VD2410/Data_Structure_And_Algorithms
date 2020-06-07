def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number < 0 or number == None:
    	return 0

    if number == 0 or number == 1 :
    	return number

    idx = 0

    result = number//2

    while(idx <= result):
    	temp = (idx+result)//2

    	if temp * temp < number:
    		idx = temp+1
    		sq=temp
    	elif temp*temp>number:
    		result=temp-1
    	else:
    		return temp


    return sq
print("--------------------------------------------Test 1--------------------------------------")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print("--------------------------------------------Test 2--------------------------------------")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print("--------------------------------------------Test 3--------------------------------------")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print("--------------------------------------------Test 4--------------------------------------")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print("--------------------------------------------Test 5--------------------------------------")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

print("--------------------------------------------Test 6--------------------------------------")
print ("Pass" if  (0 == sqrt(-1)) else "Fail")

print("--------------------------------------------Test 7--------------------------------------")
print ("Pass" if  (10540 == sqrt(111111111)) else "Fail")
