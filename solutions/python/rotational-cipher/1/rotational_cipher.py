from string import ascii_lowercase


def rotate(text: str, key: int) -> str:
    """Rotate characters in text by key positions in the alphabet.

    Args:
        text (str): The input string to be rotated.
        key (int): The number of positions to rotate each character.

    Returns:
        str: The rotated string.
    """
    rotated_str = ""
    alphabet_len = len(ascii_lowercase)
    for char in text:
        current_index = ascii_lowercase.find(char.lower())

        if current_index != -1:
            new_char = ascii_lowercase[(current_index + key) % alphabet_len]
            if char.isupper():
                new_char = new_char.upper()
        else:
            new_char = char

        rotated_str += new_char

    return rotated_str
