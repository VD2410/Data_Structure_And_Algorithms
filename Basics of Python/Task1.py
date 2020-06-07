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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

list_num = list([item[0] for item in texts]) + list([item[1] for item in texts]) + list([item[0] for item in calls]) + list([item[1] for item in calls])  # ''' Complexity n + n + n + n'''


unique = len(set(list_num)) # ''' Complexity 1'''

print("There are ",unique," different telephone numbers in the records.") # ''' Complexity 1'''

""" Complexity O(n) """