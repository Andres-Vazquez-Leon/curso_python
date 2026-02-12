"""Docstring for game_tournament."""

import random
import json
from Team import Team
from Sport import Sport
from Athlete import Athlete 

class Game:
    """Game class represents a game in the tpurnament. It has two """ #

    def __init__(self, A:Team, B:Team):
        """Custom constructo for Game class."""
        self.set_team(A, "local")
        self.set_team(B, "visitor")
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
        """Simulate playing the game by randomly assignin scores to each team"""
        self.score[self.team_a.name] = random.randint(0,
        Sport.max_score[self.team_a.sport.name])
        self.score[self.team_b.name] = random.randint(0,
        Sport.max_score[self.team_b.sport.name])

    def __str__(self):
        """String representation of the Game class."""
        return f"{self.team_a.name} vs {self.team_b.name} - Score: {self.score[self.team_a.name]: {self.score[self.team_b.name]}}" 
    def __repr__(self):
        """String representation of the Game class"""
        return f"Game(team_a={repr(self.team_a)}, team_b={repr(self.team_b)}, score={self.score})"
    def to_json(self):
        """Convert the game objecct to a JSON string"""
        return{
            "team_a": self.team_a.to_json(),
            "team_b": self.team_b.to_json(),
            "score": self.score
        }
        
        
def a_game():
    """Example usage if the Game class"""
    Players_mex = ['Chicharito', 'Piojo', 'Guardado', 'Hector Moreno', 'Rafa Marquez', 'Salcido', 'Vela', 'Dos Santos', 'Herrera', 'Layun', 'Corona']
    Players_arg = ['Messi', 'DI Maria', 'Aguero', 'Higuain', 'Mascherano', 'Biglia', 'Dybala', 'Paredes', 'Tagliafico', 'Otamendi', 'Zabaleta']
    sport = Sport("Futbol", 10, "FIFA")
    team_mex = Team("Mexico", sport)
    team_arg = Team("Argentina", sport)
    for player in Players_mex:
        team_mex.add_athlete(Athlete(player))
    for player in Players_arg:
        team_arg.add_athlete(Athlete(player))
    game = Game (team_mex, team_arg)
    game_string = game.to_json()
    print(game_string)

def save_game_to_json(game_data, filename):
    """Save the game object to a JSON file"""
    with open(filename, 'w', encoding='utf-8') as f: json.dump(game_data, f, indent = 4)

if __name__ == "__main__":
    string_game = a_game()
    save_game_to_json(string_game, "game.json")
    
    # a = Athlete("Lionel Meesi")
    # b = Athlete("Diego Armando")
    # s = Sport("Futbol", 11, "FIFA")
    # argentina = Team("Argentina", s)
    # argentina.add_athlete(a)
    # argentina.add_athlete(b)
    # brazil = Team("Brazil", s)
    # brazil.add_athlete(Athlete("Pele"))
    # brazil.add_athlete(Athlete("Zico"))
    # game = Game(argentina, brazil)
    # game.play()
    # print(game)