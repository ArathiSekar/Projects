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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
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
blr_area_code = "(080)"
list_of_codes = set()
mobile_start_digits = ['7','8','9']
call_from_blr_area_code = 0
call_to_blr_area_code = 0

for row in calls:
    if(row[0].startswith(blr_area_code)):
        call_from_blr_area_code += 1
        
        if (row[1].startswith(blr_area_code)):
            call_to_blr_area_code+=1
        
        #Checking for fixed lines
        if (row[1][0:1] == '('):
            x = row[1].index(")")
            list_of_codes.add(row[1][:x+1])
        #Checking for mobile numbers    
        elif (row[1][0:1] in mobile_start_digits):
            list_of_codes.add(row[1][:4])
        #Checking Telemarketers
        elif (row[1][0:3] == '140'):
            list_of_codes.add(row[1][0:3])
            
        
print("The numbers called by people in Bangalore have codes:")

for blr_code in sorted(list(list_of_codes)):
    print(blr_code)
    
perc_blr_calls = round((call_to_blr_area_code)*100/(call_from_blr_area_code),2)
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(perc_blr_calls))
