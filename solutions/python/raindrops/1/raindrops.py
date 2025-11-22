def convert(number: int) -> str:
    """Convert a number to a raindrop sound string.
    - If the number has 3, 5, or 7 as a factor, add 'Pling', 'Plang', or 'Plong' respectively.
    - If none of these factors are present, return the number as a string.

    Args:
        number (int): The number to convert.

    Returns:
        str: The raindrop sound string or the number as a string.
    """
    raindrop_sounds = ""

    if number % 3 == 0:
        raindrop_sounds += "Pling"

    if number % 5 == 0:
        raindrop_sounds += "Plang"

    if number % 7 == 0:
        raindrop_sounds += "Plong"

    return str(number) if not raindrop_sounds else raindrop_sounds
