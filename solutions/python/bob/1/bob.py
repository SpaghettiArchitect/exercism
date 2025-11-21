def response(hey_bob: str) -> str:
    """Generate Bob's reply to a given message.

    Args:
        hey_bob (str): The input string directed to Bob.

    Returns:
        str: Bob's response based on the input.
    """
    hey_bob = hey_bob.strip()

    if hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!" if hey_bob.isupper() else "Sure."

    if hey_bob.isupper():
        return "Whoa, chill out!"

    if hey_bob == "":
        return "Fine. Be that way!"

    return "Whatever."
