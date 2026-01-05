from datetime import datetime, timedelta


def add(moment: datetime) -> datetime:
    """Add a gigasecond (1,000,000,000 seconds) to the given datetime moment.

    Args:
        moment (datetime): The original datetime moment.

    Returns:
        datetime: A new datetime moment with a gigasecond added.
    """
    return moment + timedelta(seconds=1e9)
