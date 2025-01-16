import random

class BoardGameMaterial:
    """Class used to store all board game materials in one place."""
    pass

class Die(BoardGameMaterial):
    """Class to represent a single die."""

    def __init__(self):
        """Initialize the die with a random value between 1 and 6."""
        self.value = random.randint(1, 6)
        
    def __str__(self):
        """Return a string representation of the die's value."""
        return f"Dice shows {self.value}"
