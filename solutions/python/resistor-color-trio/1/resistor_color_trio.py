def label(colors: list[str]) -> int:
    """Return the resistance value of a resistor given its color bands. Only the first
    three colors are considered.

    Args:
        colors (list[str]): A list of color names representing the resistor bands.

    Returns:
        int: The resistance value in ohms, kiloohms, megaohms, or gigaohms.
    """
    COLORS = {
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

    band_1, band_2, zeroes, *_ = colors

    total_value = (COLORS[band_1] * 10 + COLORS[band_2]) * 10 ** COLORS[zeroes]

    trios_of_zeroes = 0
    while True:
        if (new_value := total_value // 1000) > 0:
            total_value = new_value
            trios_of_zeroes += 1
        else:
            break

    metric_prefix = ""
    match trios_of_zeroes:
        case 1:
            metric_prefix = "kilo"
        case 2:
            metric_prefix = "mega"
        case 3:
            metric_prefix = "giga"

    return f"{total_value} {metric_prefix}ohms"
