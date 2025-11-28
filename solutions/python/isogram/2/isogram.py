def is_isogram(string: str) -> bool:
    """Check if a word or sentence is an isogram. An isogram is a word or phrase
    without a repeating letter, ignoring spaces and hyphens.

    Args:
        string (str): The word or phrase to check.

    Returns:
        bool: True if the word or phrase is an isogram, False otherwise.
    """
    # A more idiomatic solution using list comprehension and set
    clean_string = "".join([letter.lower() for letter in string if letter.isalpha()])
    return len(set(clean_string)) == len(clean_string)
