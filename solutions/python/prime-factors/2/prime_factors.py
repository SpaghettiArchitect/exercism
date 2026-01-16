def factors(value: int) -> list[int]:
    """Return the prime factors of the given value.

    Args:
        value (int): The integer to factorize.

    Returns:
        list[int]: A list of prime factors.
    """
    prime_factors = []
    # Handle factor 2, this halves the number of iterations needed later.
    while value % 2 == 0:
        prime_factors.append(2)
        value //= 2

    # Check odd factors up to sqrt(value).
    divisor = 3
    while divisor * divisor <= value:
        while value % divisor == 0:
            prime_factors.append(divisor)
            value //= divisor
        divisor += 2

    # If remaining value is a prime number greater than 2, add it to the list.
    if value > 1:
        prime_factors.append(value)

    return prime_factors
