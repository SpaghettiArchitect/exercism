def reverse(text: str) -> str:
    """Reverses the given string.

    Args:
        text (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    reversed_str = ""
    current_char = len(text) - 1
    while current_char >= 0:
        reversed_str += text[current_char]
        current_char -= 1

    return reversed_str
