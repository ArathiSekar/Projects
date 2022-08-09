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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
telephone_number_dict = {}

def createDict():
    for row in calls:
        
        if((row[0] not in telephone_number_dict)):
            telephone_number_dict[row[0]] = int(row[3])
        else:
            telephone_number_dict[row[0]] += int(row[3])
    
        if (row[1] not in telephone_number_dict):
            telephone_number_dict[row[1]] = int(row[3])
        else:
            telephone_number_dict[row[1]] += int(row[3])

    return (telephone_number_dict)

telephone_number_dict = createDict()

high_duration = list(telephone_number_dict.items())[0][1]


for duration_key,duration_value in telephone_number_dict.items():
    if (duration_value >= high_duration):
        high_duration = duration_value
        telephone_number = duration_key

print ("{} spent the longest time, {} seconds, on the phone during September 2016.".format(telephone_number,high_duration))
        

