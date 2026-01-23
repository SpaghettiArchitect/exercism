UNIQUE = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

TENS = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]


def say(number: int) -> str:
    """Convert a number into its English words representation.

    Args:
        number (int): The number to convert. Must be between 0 and 999,999,999,999 inclusive.

    Returns:
        str: The English words representation of the number.

    Raises:
        ValueError: If the number is negative or larger than 999,999,999,999.
    """
    # if the number is negative or larger than 999,999,999,999
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    scales = [
        (1_000_000_000, "billion"),
        (1_000_000, "million"),
        (1_000, "thousand"),
        (1, ""),
    ]

    parts = []
    for scale, name in scales:
        if number >= scale:
            part = number // scale
            number %= scale
            part_words = part_to_words(part)
            if part_words:
                if name:
                    parts.append(f"{part_words} {name}")
                else:
                    parts.append(part_words)

    return " ".join(parts).strip()


def part_to_words(number: int) -> str:
    """Convert a number less than 1000 into words.

    Args:
        number (int): The number to convert. Must be between 0 and 999 inclusive.

    Returns:
        str: The English words representation of the number.
    """
    if number == 0:
        return ""

    parts = []

    if number >= 100:
        parts.append(f"{UNIQUE[number // 100]} hundred")
        number %= 100

    if number >= 20:
        if number % 10 == 0:
            parts.append(TENS[number // 10])
        else:
            parts.append(f"{TENS[number // 10]}-{UNIQUE[number % 10]}")
    else:
        parts.append(UNIQUE[number])

    return " ".join(parts)
