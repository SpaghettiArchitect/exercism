def score(x: int, y: int) -> int:
    """Calculate the score for a dart given its (x, y) coordinates.
    The dartboard consists of three concentric circles:

    - Inner circle (radius 1) scores 10 points.
    - Middle circle (radius 5) scores 5 points.
    - Outer circle (radius 10) scores 1 point.

    Any dart that lands outside the outer circle scores 0 points.

    Args:
        x (int): The x-coordinate of the dart.
        y (int): The y-coordinate of the dart.

    Returns:
        int: The score based on the dart's position.
    """
    # Pairs of circle radius and their points.
    targets = {
        1: 10,  # Inner circle
        5: 5,  # Middle circle
        10: 1,  # Outer cirlce
    }

    # Loops from inner to outer circle (smallest to largest circle)
    for radius in sorted(targets):
        # Calculate if the coordinate is inside of the circle given by the radius
        # using the equation (x - center_x)^2 + (y - center_y)^2 <= radius^2.
        # All circles are concentric at (0, 0), so center_x and center_y can be omitted.
        if (x**2 + y**2) <= (radius**2):
            return targets[radius]

    return 0  # The coordinate doesn't fall inside any of the circles.
