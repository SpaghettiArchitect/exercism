from string import ascii_lowercase

CIPHER = {char: ascii_lowercase[-(i + 1)] for i, char in enumerate(ascii_lowercase)}


def encode(plain_text: str) -> str:
    """Encode the given plain text using the Atbash cipher.

    - Non-alphanumeric characters are ignored in the encoding process.
    - The output is grouped in blocks of five characters separated by spaces.

    Args:
        plain_text (str): The text to be encoded.

    Returns:
        str: The encoded text.
    """
    counter = 0
    encoded_text = ""
    for char in plain_text.lower():
        if not char.isalnum():
            continue

        encoded_text += CIPHER[char] if char.isalpha() else char

        counter += 1
        if counter >= 5:
            counter = 0
            encoded_text += " "

    return encoded_text.strip()


def decode(ciphered_text: str) -> str:
    """Decode the given ciphered text using the Atbash cipher.

    - Non-alphanumeric characters are ignored in the decoding process.

    Args:
        ciphered_text (str): The text to be decoded.

    Returns:
        str: The decoded text.
    """
    return "".join(
        [
            CIPHER[char] if char.isalpha() else char
            for char in ciphered_text
            if char.isalnum()
        ]
    )
