def find(search_list: list[int], value: int) -> int:
    """Perform a binary search to find the index of `value` in `search_list`.

    Args:
        search_list (list[int]): A sorted list of integers to search.
        value: An integer value to find in `search_list`.

    Returns:
        int: The index of `value` in `search_list`.

    Raises:
        ValueError: If `value` is not found in `search_list`.
    """
    if not search_list:
        raise ValueError("value not in array")

    middle_index = len(search_list) // 2
    middle_value = search_list[middle_index]
    if middle_value == value:
        return middle_index

    if middle_value > value:
        return find(search_list[:middle_index], value)

    if middle_value < value:
        return middle_index + 1 + find(search_list[middle_index + 1 :], value)
