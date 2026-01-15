from math import sqrt


def factors(value: int) -> list[int]:
    """Return the prime factors of the given value.

    Args:
        value (int): The integer to factorize.

    Returns:
        list[int]: A list of prime factors.
    """
    primes = calculate_primes(round(sqrt(value)))

    factors = []
    tmp_value = value
    for prime in primes:
        while tmp_value % prime == 0:
            tmp_value /= prime
            factors.append(prime)

    return factors if factors else [value]


def calculate_primes(n: int) -> list[int]:
    """Calculate all prime numbers up to n using the Sieve of Eratosthenes.

    Args:
        n (int): The upper limit to calculate primes.

    Returns:
        list[int]: A list of prime numbers up to n.
    """
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False

    p = 2
    while (p**2) <= n:
        if primes[p]:
            for i in range(p**2, n + 1, p):
                primes[i] = False

        p += 1

    return [i for i, prime in enumerate(primes) if prime]
