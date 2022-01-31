'''
AUTHOR: ADNAN SAMI
ID    : 19-39676-1
'''
# INPUT ID HERE
ID = '19-39676-1'

isNumeric = False # INITIALIZING FALSE
T = '' # EMPTY STRING
i = 0
while i < 10:
    if ID[i] != '-':
        T += ID[i] # CONCATENATING STRING
    i += 1


if T.isnumeric():
    isNumeric = True # IF NUMERIC SET TRUE

# PRINTING DECISION
if isNumeric:
    print ("Numeric")
else:
    print ("Non-Numeric")
