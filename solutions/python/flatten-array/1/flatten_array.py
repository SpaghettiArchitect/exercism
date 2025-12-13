def flatten(iterable: list) -> list:
    """Flattens a nested array. Omits null values (None).

    Args:
        iterable (list): A potentially nested list of elements. Elements can be of any type.

    Returns:
        list: A flattened list with all null values removed.
    """
    flattened_array = []
    for element in iterable:
        if element is None:
            continue
        if isinstance(element, type(list())):
            flattened_array.extend(flatten(element))
        else:
            flattened_array.append(element)

    return flattened_array
