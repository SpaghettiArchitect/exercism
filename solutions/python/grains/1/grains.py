def square(number: int) -> int:
    """Calculate the number of grains on a given square of the chess board.

    Args:
        number (int): An integer between 1 and 64

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
    total_sum = 0
    for number in range(1, 65):
        total_sum += square(number)
    return total_sum
