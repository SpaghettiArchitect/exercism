def is_paired(input_string: str) -> bool:
    cleaned_str = "".join([char for char in input_string if char in "()[]{}"])

    if len(cleaned_str) % 2 != 0:
        return False

    return check_all_pairs(cleaned_str)


def check_all_pairs(cleaned_str: str) -> bool:
    if len(cleaned_str) == 0:
        return True

    if (
        (cleaned_str.startswith("(") and not cleaned_str.endswith(")"))
        or (cleaned_str.startswith("[") and not cleaned_str.endswith("]"))
        or (cleaned_str.startswith("{") and not cleaned_str.endswith("}"))
    ):
        return False

    return check_all_pairs(cleaned_str[1:-1])
