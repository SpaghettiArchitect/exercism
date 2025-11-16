"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    seats = ("A", "B", "C", "D")
    for seat_number in range(number):
        yield seats[seat_number % len(seats)]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    all_seat_letters = generate_seat_letters(number)

    seats_per_row = 4
    current_row = 1
    for seat_letter in all_seat_letters:
        if seats_per_row <= 0:
            seats_per_row = 4
            if current_row + 1 != 13:
                current_row += 1
            else:
                current_row += 2
        yield f"{current_row}{seat_letter}"
        seats_per_row -= 1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    passengers_with_seats = {}
    all_seats = generate_seats(len(passengers))
    for passenger in passengers:
        passengers_with_seats[passenger] = next(all_seats)

    return passengers_with_seats


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat_number in seat_numbers:
        yield f"{seat_number}{flight_id}".ljust(12, "0")
