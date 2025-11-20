def steps(number):
    """Calculate the number of steps to reach 1 according with the rules of the Collatz Conjecture.

    The rules are as follow:
    - If it's even, divide it by 2.
    - If it's odd, multiply it by 3 and add 1.

    Args:
        number (int): a positive integer to calculate the number of steps to reach 1.

    Returns:
        int: The number of steps it took to reach the number 1 according to the conjecture.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    total_steps = 0
    while number > 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        total_steps += 1

    return total_steps
