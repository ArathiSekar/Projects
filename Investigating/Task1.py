"""
Read file into texts and calls.

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
telephone_records = set()

for row in texts:
    telephone_records.add(row[0])
    telephone_records.add(row[1])

for row in calls:
    telephone_records.add(row[0])
    telephone_records.add(row[1])

print("There are {} different telephone numbers in the records.".format(len(list(telephone_records))))
