"""Docstring for game_tournament."""

import random
from Team import Team
from Sport import Sport
from Athlete import Athlete 

class Game:
    """Game class represents a game in the tpurnament. It has two """ #

    def __init__(self, A:Team, B:Team):
        """Custom constructo for Game class."""
        self.set_team_a(A, "local")
        self.set_team_b(B, "visitor")
        self.score = {
            A.name: 0, B.name: 0
        }

    def set_team(self, team, role):
        """Set team A for the game"""
        if isinstance(team, Team):
            if role == "local":
                self.team_a = team
            elif role == "visitor":
                self.team_b = team
            else:
                raise ValueError ("Role must be 'local' or 'visitor'.")
        else:
            raise ValueError ("Only Team objetcts can be set as a team.")
        
    def play(self):
        """Simulate playin the game by randomly assignin scores to each team"""
        self.score[self.team_a.name] = random.randint(0,
        Sport.max_score[self.team_a.sport.name])
        self.score[self.team_b.name] = random.randint(0,
        Sport.max_score[self.team_b.sport.name])
        self.set_team_a(A)
        self.set_team_b(B)
        self.score = {
            A.name: 0, B.name: 0
        }

        def __str__(self):
            """String representation of the Game class."""
            return f"{self.team_a.name} vs {self.team_b.name} - Score: {self.score[self.team_a.name]: {self.score[self.team_b.name]}}" 
        
if __name__ == "__main__":
    a = Athlete("Lionel Meesi")
    b = Athlete("Diego Armando")
    s = Sport("Futbol", 11, "FIFA")
    argentina = Team("Argentina", s)
    argentina.add_athlete(a)
    argentina.add_athlete(b)
    brazil = Team("Brazil", s)
    brazil.add_athlete(Athlete("Pele"))
    brazil.add_athlete(Athlete("Zico"))
    game = Game(argentina, brazil)
    game.play()
    print(game)