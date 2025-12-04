def resistor_label(colors: list[str]) -> str:
    """Translates resistor color bands into a human-readable label.

    It takes either 1, 4, or 5 color bands. The first two or three bands
    represent significant digits, the next band is the multiplier, and the last
    band is the tolerance.

    Args:
        colors (list[str]): A list of color bands on the resistor.

    Returns:
        str: A formatted string representing the resistance value and tolerance.
    """
    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"

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

    TOLERANCE_BANDS = {
        "grey": 0.05,
        "violet": 0.1,
        "blue": 0.25,
        "green": 0.5,
        "brown": 1,
        "red": 2,
        "gold": 5,
        "silver": 10,
    }

    *values, multiplier, tolerance = colors
    tolerance = TOLERANCE_BANDS[tolerance]

    if len(values) == 2:
        total_value = COLOR_BANDS[values[0]] * 10 + COLOR_BANDS[values[1]]
    else:
        total_value = (
            COLOR_BANDS[values[0]] * 100
            + COLOR_BANDS[values[1]] * 10
            + COLOR_BANDS[values[2]]
        )

    total_value *= 10 ** COLOR_BANDS[multiplier]

    trios_of_zeroes = 0
    tmp_total_value = total_value
    while True:
        if (new_value := tmp_total_value / 1000) >= 1:
            tmp_total_value = new_value
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

    if round(tmp_total_value) == tmp_total_value:
        tmp_total_value = round(tmp_total_value)

    return f"{tmp_total_value} {metric_prefix}ohms ±{tolerance}%"
