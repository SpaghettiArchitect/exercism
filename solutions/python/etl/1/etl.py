def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    """Transform legacy data format to new data format.

    Args:
        legacy_data (dict[int, list[str]]): The legacy data format where keys are points
            and values are lists of uppercase letters.

    Returns:
        new_data_format (dict[str, int]): The new data format where keys are lowercase
            letters and values are points.
    """
    new_data_format = {}
    for points, letter_list in legacy_data.items():
        for letter in letter_list:
            new_data_format[letter.lower()] = points

    return new_data_format
