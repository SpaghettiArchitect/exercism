def append(list1: list, list2: list) -> list:
    return list1 + list2 if isinstance(list2, list) else list1 + [list2]


def concat(lists: list[list]) -> list:
    flattened_list = []
    for list in lists:
        flattened_list = append(flattened_list, list)

    return flattened_list


def filter(function, list: list) -> list:
    filtered_list = []
    for item in list:
        if function(item):
            filtered_list = append(filtered_list, item)

    return filtered_list


def length(list: list) -> int:
    counter = 0
    for _ in list:
        counter += 1

    return counter


def map(function, list):
    mapped_list = []
    for item in list:
        mapped_list = append(mapped_list, function(item))

    return mapped_list


def foldl(function, list: list, initial: int):
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, list, initial):
    return foldl(function, reverse(list), initial)


def reverse(list: list) -> list:
    reversed_list = []
    index = length(list) - 1

    while index >= 0:
        reversed_list = append(reversed_list, list[index])
        index -= 1

    return reversed_list
