def square_of_sum(number: int) -> int:
    """Calculate the square of the sum of the first 'number' natural numbers.

    Reference: https://www.cuemath.com/sum-of-natural-numbers-formula/

    Args:
        number (int): The upper limit of the range of natural numbers.

    Returns:
        int: The square of the sum of the first 'number' natural numbers.
    """
    return ((number * (number + 1)) // 2) ** 2


def sum_of_squares(number: int) -> int:
    """Calculate the sum of the squares of the first 'number' natural numbers.

    Reference: https://www.cuemath.com/algebra/sum-of-squares/

    Args:
        number (int): The upper limit of the range of natural numbers.

    Returns:
        int: The sum of the squares of the first 'number' natural numbers.
    """
    return (number * (number + 1) * (2 * number + 1)) // 6


def difference_of_squares(number: int) -> int:
    """Calculate the difference between the square of the sum and the sum of the
    squares of the first 'number' natural numbers.

    Args:
        number (int): The upper limit of the range of natural numbers.

    Returns:
        int: The difference between the square of the sum and the sum of the squares.
    """
    return square_of_sum(number) - sum_of_squares(number)
