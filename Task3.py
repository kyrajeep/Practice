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


# PART A ##########################
def filter(calls):
    # this function goes through 'calls.txt' and identifies data with the origin from Bangalore.
    bangalore = list()
    for call in calls: 
        if call[0].startswith('(080)'):
            bangalore.append(call[1])
    return bangalore

         
def areacode(bangalore):
    '''
    Depending on the type of phone number, add the area code to 
    the list if it is not a duplicate
    '''
    code_list = list()
    for phone_n in bangalore:
        
        if phone_n.startswith('('):
            end = iter_fixed(phone_n)
            temp = phone_n[0:end+1]
            if temp not in code_list:
                code_list.append(temp)
        
        elif phone_n.startswith('7' or '8' or '9'):
            
            end = iter_mobile(phone_n)
            temp = phone_n[0:end]
            if temp not in code_list:
                code_list.append(temp) 
        else:
            temp = '140'            
            if temp not in code_list:
                code_list.append(temp) 
            
    return code_list
    
def iter_fixed(phone_n):
    # extracting area code for fixed numbers
    i=0
    while phone_n[i] != ")":
    
        i = i+ 1
    return i
def iter_mobile(phone_n):
    # extracting area code for mobile numbers
    i=0
    while phone_n[i] != " ":
        i = i+1
    return i

def printline():
    # prints codes one for each line.
    # RUNTIME ANALYSIS: The whole program is run in O(n^2log(n)) time because 
    # all functions are in O(n) but I run sorted on top of that? -> Question.
    codes = sorted(areacode(filter(calls)))
    for i in codes:
        print(i)



# PART B ##########################
# Time complexity: O(n)
def bangalore(calls):
    '''
    counts the number of from Bangalore to Bangalore calls and calculates the percentage
    '''
    bangalore_num = 0
    for item in calls:
        
        if item[0].startswith('(080)') and item[1].startswith('(080)'):
            bangalore_num += 1
    return bangalore_num / len(calls) * 100

if __name__ == "__main__":
    print("The numbers called by people in Bangalore have codes:")
    printline()
    print(str("{0:.2f}".format(bangalore(calls))) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
