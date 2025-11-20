def is_armstrong_number(number):
    """Check if the given number is an Armstrong number. An Armstrong number
    is a number that is the sum of its own digits each raised to the power
    of the number of digits.

    Args:
        number (int): The number to check if it is an Armstrong number.

    Returns:
        bool: True if the given number is an Armstrong number, False otherwise.
    """
    number_of_digits = len(str(number))
    total_sum = 0
    for digit in str(number):
        total_sum += int(digit) ** number_of_digits

    return number == total_sum
