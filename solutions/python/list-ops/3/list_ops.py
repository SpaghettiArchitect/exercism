def append(list1: list, list2: list) -> list:
    """Appends list2 to the end of list1 and returns the new list."""
    return list1 + list2


def concat(lists: list[list]) -> list:
    """Concatenates a list of lists into a single list."""
    flattened_list = []
    for list in lists:
        flattened_list = append(flattened_list, list)

    return flattened_list


def filter(function: callable, list: list) -> list:
    """Filters the list by applying the function to each element and
    including only those elements for which the function returns True."""
    filtered_list = []
    for item in list:
        if function(item):
            filtered_list = append(filtered_list, [item])

    return filtered_list


def length(list: list) -> int:
    """Returns the length of the list."""
    counter = 0
    for _ in list:
        counter += 1

    return counter


def map(function: callable, list: list) -> list:
    """Applies the function to each element of the list and returns a new list
    with the results."""
    mapped_list = []
    for item in list:
        mapped_list = append(mapped_list, [function(item)])

    return mapped_list


def foldl(function: callable, list: list, initial: int) -> int:
    """Folds the list from the left using the provided function and initial value."""
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function: callable, list: list, initial: int) -> int:
    """Folds the list from the right using the provided function and initial value."""
    return foldl(function, reverse(list), initial)


def reverse(list: list) -> list:
    """Reverses the list and returns the new list."""
    reversed_list = []
    index = length(list) - 1

    while index >= 0:
        reversed_list = append(reversed_list, [list[index]])
        index -= 1

    return reversed_list
