def is_isogram(string: str) -> bool:
    """Check if a word or sentence is an isogram. An isogram is a word or phrase
    without a repeating letter, ignoring spaces and hyphens.

    Args:
        string (str): The word or phrase to check.

    Returns:
        bool: True if the word or phrase is an isogram, False otherwise.
    """
    # We don't need to recalculate this every time.
    string = string.lower()
    str_len = len(string)

    for i, letter in enumerate(string):
        # Ignore spaces and hyphens.
        if letter in [" ", "-", "_"]:
            continue

        # Check we haven't reached the end of the string and that the current
        # letter doesn't appear in the rest of the string
        if i + 1 != str_len and letter in string[i + 1 :]:
            return False

    return True
