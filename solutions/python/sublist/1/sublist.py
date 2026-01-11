"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one: list, list_two: list) -> int:
    """Determine if list_one is a sublist, superlist, equal to, or unequal to list_two.

    Args:
        list_one (list): The first list to compare.
        list_two (list): The second list to compare.

    Returns:
        int: One of the enumerated constants SUBLIST, SUPERLIST, EQUAL, UNEQUAL.
    """
    if list_one == list_two:
        return EQUAL

    list_one_str = str(list_one).strip("[]") + ","
    list_two_str = str(list_two).strip("[]") + ","

    if list_one_str in list_two_str:
        return SUBLIST

    if list_two_str in list_one_str:
        return SUPERLIST

    return UNEQUAL
