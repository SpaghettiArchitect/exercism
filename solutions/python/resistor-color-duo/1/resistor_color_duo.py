def value(colors: list[str]) -> int:
    """Calculate the resistance value based on the first two color bands. Each color corresponds to a digit.

    Args:
        colors (list[str]): A list of color names representing the bands on the resistor.

    Returns:
        int: The resistance value formed by the first two color bands.
    """
    COLOR_BANDS = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    color_1, color_2, *_ = colors

    return COLOR_BANDS[color_1] * 10 + COLOR_BANDS[color_2]
