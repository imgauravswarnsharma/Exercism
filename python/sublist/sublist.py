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
SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'
def sublist(list_one, list_two):
    len_1 = len(list_one)
    len_2 = len(list_two)
    len_x = abs(len_1-len_2)

    if list_one == list_two:
        return EQUAL

    if len_1>len_2:
        if not list_two :
            return SUPERLIST
        for i in range(len_x+1):
            if list_one[i:i+len_2] == list_two:
                return SUPERLIST

    if len_2>len_1:
        if not list_one :
            return SUBLIST
        for i in range(len_x+1):
            if list_one ==list_two[i:i+len_1]:
                return SUBLIST
    return UNEQUAL