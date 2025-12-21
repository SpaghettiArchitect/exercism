class SpaceAge:
    """Calculate age on different planets based on seconds lived."""

    def __init__(self, seconds: int):
        """Initialize with age in seconds."""
        self.age_in_seconds = seconds

    def get_age_in_planet(self, planet: str) -> float:
        """Calculate age on a given planet."""
        earth_year_in_seconds = 31_557_600
        orbital_periods = {
            "mercury": 0.2408467,
            "venus": 0.61519726,
            "earth": 1.0,
            "mars": 1.8808158,
            "jupiter": 11.862615,
            "saturn": 29.447498,
            "uranus": 84.016846,
            "neptune": 164.79132,
        }
        planet_year_in_seconds = earth_year_in_seconds * orbital_periods[planet]
        return round(self.age_in_seconds / planet_year_in_seconds, 2)

    def on_mercury(self) -> float:
        """Calculate age on Mercury."""
        return self.get_age_in_planet("mercury")

    def on_venus(self) -> float:
        """Calculate age on Venus."""
        return self.get_age_in_planet("venus")

    def on_earth(self) -> float:
        """Calculate age on Earth."""
        return self.get_age_in_planet("earth")

    def on_mars(self) -> float:
        """Calculate age on Mars."""
        return self.get_age_in_planet("mars")

    def on_jupiter(self) -> float:
        """Calculate age on Jupiter."""
        return self.get_age_in_planet("jupiter")

    def on_saturn(self) -> float:
        """Calculate age on Saturn."""
        return self.get_age_in_planet("saturn")

    def on_uranus(self) -> float:
        """Calculate age on Uranus."""
        return self.get_age_in_planet("uranus")

    def on_neptune(self) -> float:
        """Calculate age on Neptune."""
        return self.get_age_in_planet("neptune")
