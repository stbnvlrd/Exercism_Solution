"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def equal(list_one, list_two):
    count = 0
    for index in range(len(list_one)):
        if list_one[index] == list_two[index]:
            count = count + 1
    if count == len(list_one):
        result = EQUAL
    else:   
        result = UNEQUAL
    return result
    
def sublist(list_one, list_two):
    lenght_A = len(list_one)
    lenght_B = len(list_two)
    if lenght_A == lenght_B:
        result = equal(list_one, list_two)
    # elif lenght_A < lenght_B:
    # elif lenght_A > lenght_B:

    return result