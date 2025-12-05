def commands(binary_str: str) -> list[str]:
    """Convert a binary string to a list of secret handshake commands.

    Args:
        binary_str (str): A string representing a binary number.

    Returns:
        list[str]: A list of commands corresponding to the binary input.
    """
    all_actions = ["wink", "double blink", "close your eyes", "jump"]
    current_actions = []
    for i, digit in enumerate(reversed(binary_str)):
        if digit == "1":
            if i != 4:
                current_actions.append(all_actions[i])
            else:
                current_actions.reverse()

    return current_actions
