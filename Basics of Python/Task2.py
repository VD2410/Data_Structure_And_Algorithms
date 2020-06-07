"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


# list_num = list([item[0] for item in texts])

list_num = list([item[0] for item in calls]) + list([item[1] for item in calls])  # ''' Complexity n + n + n + n'''


unique = list(set(list_num))

time_dict = defaultdict(list)

for num in unique:

	time_dict[num]=0
# time_dict = {unique:0}

# print(time_dict)




time_spent = list([int(item[3]) for item in calls])	# ''' Complexity n'''
# # print(time_spent)
# max_time = time_spent[0]	# ''' Complexity 1'''
# idx = 0	# ''' Complexity 1'''



for i in range(0,len(time_spent)):	# ''' Complexity n'''

	time_dict[calls[i][0]] += time_spent[i] # ''' Complexity n'''

	time_dict[calls[i][1]] += time_spent[i] # ''' Complexity n'''

max_time = [unique[0],time_dict[unique[0]]]

for i in unique:

	if time_dict[i] > max_time[1]:

		max_time[0] = i
		max_time[1] = time_dict[i]


print(max_time[0]," spent the longest time, ",max_time[1]," seconds, on the phone during September 2016.") # ''' Complexity 1'''


# ''' Complexity O(n)'''