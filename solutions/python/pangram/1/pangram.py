def is_pangram(sentence: str) -> bool:
    """
    Check if the given sentence is a pangram. A sentence is a pangram
    if it uses every letter in the alphabet at least once.

    :param sentence: The sentence to check.
    :type sentence: str

    :return: True if the sentence is a pangram, False otherwise.
    :rtype: bool
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in alphabet:
        if letter not in sentence.upper():
            return False

    return True
