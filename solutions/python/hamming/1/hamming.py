def distance(strand_a: str, strand_b: str) -> int:
    """Calculate the Hamming distance between two DNA strands.

    Args:
        strand_a (str): The first DNA strand.
        strand_b (str): The second DNA strand.

    Returns:
        int: The Hamming distance between the two strands.

    Raises:
        ValueError: If the strands are of unequal length.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    hamming_distance = 0
    for char_a, char_b in zip(strand_a, strand_b):
        if char_a != char_b:
            hamming_distance += 1

    return hamming_distance
