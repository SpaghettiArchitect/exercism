def is_paired(input_string: str) -> bool:
    """Determine if all types of brackets are correctly paired and nested in the input string.

    Args:
        input_string (str): The string to be checked for paired brackets.

    Returns:
        bool: True if all brackets are correctly paired and nested, False otherwise.
    """
    cleaned_input = "".join(char for char in input_string if char in "()[]{}")
    while "()" in cleaned_input or "[]" in cleaned_input or "{}" in cleaned_input:
        cleaned_input = (
            cleaned_input.replace("()", "").replace("[]", "").replace("{}", "")
        )

    return not cleaned_input
