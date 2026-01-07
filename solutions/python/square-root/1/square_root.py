def square_root(number: int | float) -> float:
    """Calculate the square root of a number using Newton's method.

    Args:
        number (int | float): A positive number.

    Returns:
        float: The square root of the number.

    """
    approximation = number / 2.0

    while True:
        if approximation <= 0:
            break

        # If a better approximation is not longer possible, end the loop.
        next_approximation = 0.5 * (approximation + (number / approximation))
        if next_approximation == approximation:
            break

        approximation = next_approximation

    return approximation
