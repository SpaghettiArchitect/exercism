def leap_year(year: int) -> bool:
    """Calculates if the given year is a leap year.

    Rules:
    - Every four years is a leap year.
    - Every 100 years the leap year is skipped, unless the century is divisible by 400.

    Args:
        year (int): the year to calculate.

    Returns:
        bool: True if the year is a leap year, False otherwise.

    """
    if (year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True

    return False
