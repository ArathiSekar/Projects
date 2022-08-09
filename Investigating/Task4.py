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
possible_tele = set()
outgoing_calls = set()
incoming_calls = set()
outgoing_texts = set()
incoming_texts = set()

for call_row in calls:
    outgoing_calls.add(call_row[0])
    incoming_calls.add(call_row[1])


for text_row in texts:
    outgoing_texts.add(text_row[0])
    incoming_texts.add(text_row[1])


for possible_num in outgoing_calls:
    if ((possible_num not in incoming_calls) and (possible_num not in outgoing_texts) and (possible_num not in incoming_texts)):
        possible_tele.add(possible_num)

print("These numbers could be telemarketers: ")
for tele_num in (sorted(list(possible_tele))):
    print(tele_num)
