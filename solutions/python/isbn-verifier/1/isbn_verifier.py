def is_valid(isbn: str) -> bool:
    """Checks if the given string is in a valid ISBN-10 format.

    Args:
        isbn (str): the string to check.

    Returns:
        bool: True if the string is in a valid format, False otherwise.
    """
    clean_isbn = isbn.replace("-", "")

    if len(clean_isbn) != 10:
        return False

    if not clean_isbn[:-1].isdigit():
        return False

    if clean_isbn[-1].isalpha() and clean_isbn[-1] != "X":
        return False

    isbn_multiplied = [
        int(char) * (10 - i) if char != "X" else 10 for i, char in enumerate(clean_isbn)
    ]

    return sum(isbn_multiplied) % 11 == 0
