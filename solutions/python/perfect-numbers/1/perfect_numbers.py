def get_all_factors(number: int) -> list[int]:
    """Get all factors of a number excluding the number itself.

    :param number: int a positive integer
    :return: list[int] list of factors
    """
    return [factor for factor in range(1, number) if number % factor == 0]


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factors = get_all_factors(number)
    aliquot_sum = sum(factors)

    if number < aliquot_sum:
        return "abundant"

    if number > aliquot_sum:
        return "deficient"

    return "perfect"
