COLOR_BANDS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def color_code(color) -> int:
    """Return the numerical value of the given color band.

    Args:
        color (str): The color band name.

    Returns:
        int: The numerical value corresponding to the color band.
    """
    return COLOR_BANDS.index(color)


def colors() -> list[str]:
    """Return a list of all color bands.

    Returns:
        list: A list of all color band names.
    """
    return COLOR_BANDS
