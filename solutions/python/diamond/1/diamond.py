from string import ascii_uppercase


def rows(letter: str) -> list[str]:
    """Generate a diamond shape with the given letter at its widest point.

    Args:
        letter (str): A single uppercase letter from A to Z.

    Returns:
        list[str]: A list of strings representing the diamond shape.
    """
    n = ascii_uppercase.find(letter)
    top_half = []
    for i, char in enumerate(ascii_uppercase[: n + 1]):
        left_side = " " * (n - i) + char + " " * i
        right_side = left_side[:-1][::-1]
        top_half.append(left_side + right_side)

    bottom_half = reversed(top_half[:n])

    diamond_shape = [*top_half, *bottom_half]

    return diamond_shape
