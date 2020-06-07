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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


from_num = list([item[0] for item in calls])					# ''' Complexity n'''
to_num = list([item[1] for item in calls])						# ''' Complexity n'''
# print(from_num[1][:6])
area_codes = list()												# ''' Complexity 1'''
total = len(to_num)												# ''' Complexity 1'''
count_Bang_calls = 0		
									# ''' Complexity 1'''
for idx in range(0,len(from_num)):								# ''' Complexity n'''

	# print(from_num[idx][:6] )

	if from_num[idx][:5] == '(080)':							# ''' Complexity n'''
		if to_num[idx][5]==' ':									# ''' Complexity n'''
			area_codes.append(to_num[idx][:4])					# ''' Complexity m'''

		if to_num[idx][0] == '(':								# ''' Complexity n'''
			area_codes.append(to_num[idx].split(')')[0]+')')	# ''' Complexity m'''

		if to_num[idx][:3]=='140':								# ''' Complexity n'''
			area_codes.append(to_num[idx][:3])					# ''' Complexity m'''
		if to_num[idx][:5]=='(080)':							# ''' Complexity n'''
			count_Bang_calls +=1								# ''' Complexity m'''


print("The numbers called by people in Bangalore have codes:")	# ''' Complexity 1'''
print("\n".join(sorted(set(area_codes),key=str)))				# ''' Complexity n log n'''

percent = round((count_Bang_calls * 100)/ total, 2)				# ''' Complexity 1'''

print("\n\n",percent," percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")	# ''' Complexity 1'''

	# ''' Complexity O(n log n))'''