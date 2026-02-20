"""Docstring for game_tournament.Group"""
import random
from Team import Team
from Game import Game

class Group:
    """Class representing a group in the tournament"""
    def __init__(self, name):
        self.name = name
        self.teams = []
        self.games = []
        
    def add_team(self, team):
        """Add a team to the group"""
        if isinstance(team, Team):
            self.teams.append(team)
        else:
            raise ValueError("Only Team objects can be added to the team")
    def add_games(self):
        for i in range(len(group_list)):
            for j in range(i+1, len(group_list)):
                game = Game(group_list[i], group_list[j])
                self.games.append(game) 

    
    def __str__(self):
        """String representation of the Group class"""
        return f"Group: {self.name}, Teams: {len(self.teams)}"
    def __repr__(self):
        """String representation of the Group class"""
        return f"Group(name={self.name}, teams={self.teams})"
    def to_json(self):
        """Convert the Group object to a JSON string"""
        return {
            "name": self.name,
            "teams": [team.to_json() for team in self.teams]
        }
