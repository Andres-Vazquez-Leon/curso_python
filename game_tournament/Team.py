from Athlete import Athlete
from Sport import Sport

class Team:
    """Team class represents a team in the tournament.
    It has a name, a sport, and a list od athletes."""

    def __init__(self, name, sport:Sport):
        """Add an athlete to the team."""
        self.name = name
        self.sport = sport
        self.athletes = []
    
    def add_athlete(self, athlete):
        """Add an athlete to the team."""
        if isinstance(athlete, Athlete): #se
            self.athletes.append(athlete)
        else:
            raise ValueError("Only Athlete onjtect can be added to the team.")
        
if __name__  == "__main__":
    print(add_athlete("Uwu"))