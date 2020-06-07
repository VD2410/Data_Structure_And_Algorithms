"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

calls_from_num = list([item[0] for item in calls])												# ''' Complexity n'''
calls_to_num = list([item[1] for item in calls])												# ''' Complexity n'''
text_from_num = list([item[0] for item in texts])												# ''' Complexity n'''
text_to_num = list([item[1] for item in texts])													# ''' Complexity n'''

telemarketers = list()																			# ''' Complexity 1'''

for n in calls_from_num:																		# ''' Complexity n'''

	if n not in calls_to_num and n not in text_from_num and n not in text_to_num:				# ''' Complexity n'''

		telemarketers.append(n)																	# ''' Complexity m'''


print("These numbers could be telemarketers: ")													# ''' Complexity 1'''
print("\n".join(sorted(set(telemarketers),key=str)))											# ''' Complexity n log n'''


# ''' Complexity O(n log n))'''