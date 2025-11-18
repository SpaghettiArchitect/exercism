def is_triangle(sides: list[int]) -> bool:
    """Check if the given sides can form a triangle."""
    a, b, c = sides

    # No side shall be 0.
    if 0 in sides:
        return False

    return (a + b >= c) and (b + c >= a) and (a + c >= b)


def equilateral(sides: list[int]) -> bool:
    """Check if the triangle with the given sides is equilateral."""
    a, b, c = sides
    return is_triangle(sides) and (a == b == c)


def isosceles(sides: list[int]) -> bool:
    """Check if the triangle with the given sides is isosceles."""
    a, b, c = sides
    return (
        equilateral(sides)  # An equilateral triangle is also isosceles
        or is_triangle(sides)
        and ((a == b != c) or (b == c != a) or (a == c != b))
    )


def scalene(sides: list[int]) -> bool:
    """Check if the triangle with the given sides is scalene."""
    a, b, c = sides
    return is_triangle(sides) and not isosceles(sides) and (a != b != c)
