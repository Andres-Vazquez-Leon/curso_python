"""Docstring for game_tournament.Tournament"""
import random
import json
from Game import Game
from Team import Team
from Athlete import Athlete
from Sport import Sport

class Tournament:
    """Class representing a tournament"""
    def __init__(self, name):
        self.name = name
        self.sport = sport = []
        self.teams = teams  = []
    def add_team(self, team):
        """Add a team to the tournament"""
        if isinstance(team, Team):
            self.teams.append(team)
        else:
            raise ValueError("Only Team objects can be added to the tournament")
    def add_game(self, game):
        """Add a game to the tournament"""
        if isinstance(game, Game):
            self.games.append(game)
        else:
            raise ValueError("Only Game objects can be added to the tournament")
        
    def __str__(self):
        """ String representation of the Tournament class. """
        return f"Tournament: {self.name}, Teams: {len(self.teams)}, Games: {len(self.games)}"
    
    def __repr__(self):
        """String representation of the tournament object"""
        return f"Tournament(name={self.name}, teams={self.teams}, games={self.games})"
    
    def to_json(self):
        """ Convert the Tournament object to a JSON string. """
        return {
            "name": self.name,
            "teams": [team.to_json() for team in self.teams],
            "games": [game.to_json() for game in self.games]
        }

    def load_json(self, filename):
        """ Load a Tournament object from a JSON file. """
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for team_data in data["teams"]:
                team_name = team_data["name"]
                sport_name = team_data["sport"]["name"]
                sport_league = team_data["sport"]["league"]
                sport_num_players = team_data["sport"]["num_players"]
                sport = Sport(sport_name, sport_num_players, sport_league)
                team = Team(team_name, sport)
                #team = Team(team_data["name"], team["sport"])
                players = team_data["athletes"]
                
                for player in players:
                    team.add_athlete(Athlete(player))
                self.add_team(team)


if __name__ == "__main__":
    tournament = Tournament("FIFA World Cup")
    tournament.load_json("tournament.json")
    print(tournament)
                
