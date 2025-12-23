def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """Return the sum of all unique multiples of the given factors below the limit.

    Args:
        limit (int): The upper limit (exclusive).
        multiples (list[int]): A list of factors to find multiples of.

    Returns:
        int: The sum of all unique multiples of the factors below the limit.
    """
    unique_multiples = set()
    for factor in multiples:
        if factor > limit or factor == 0:
            continue
        unique_multiples.update([i for i in range(0, limit, factor)])

    return sum(unique_multiples)
