def square(number: int) -> int:
    """Calculate the number of grains on a given square of the chess board.

    Args:
        number (int): An integer between 1 and 64.

    Returns:
        int: Total number of grains in the given square.

    Raises:
        ValuError: If the given number is not in the range 1 to 64.
    """
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)


def total() -> int:
    """Calculates the sum of all the grains in a 8x8 chess board.

    Returns:
        int: total number of grains in the whole chess board.
    """
    # A better solution is using the geometric series formula:
    # a(r^n - 1) / (r - 1), where:
    # - "a" is the first term in the series,
    # - "r" is the common ration, and
    # - "n" is the number of terms to be added.
    # In this case: a = 1, r = 2, n = 64. So, replacing our values in the formula:
    # 1(2^64 - 1) / (2 - 1) -> 2^64 - 1
    return 2**64 - 1
