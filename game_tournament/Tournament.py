"""Docstring for game_tournament.Tournament"""
import random
import json
from Game import Game
from Team import Team
from Athlete import Athlete
from Sport import Sport
from Group import Group

class Tournament:
    """Class representing a tournament"""
    def __init__(self, name):
        self.name = name
        self.sport = sport = []
        self.teams = teams  = []
        self.group = 
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
    
    def set_group(self, group_list, group_name):
        """Set up the for each team in the tournament"""
        group = Group(group_name)
        for team in group_list:
            group.add_team(team)
        self.groups[group_name] = group

    def set_group_games(self, group_list):
        """Set up the games for each group in the tournament"""



        for i in range(len(group_list)):
            for j in range(i+1, len(group_list)):
                game = Game(group_list[i], group_list[j])
                self.add_game(game) 

    def set_group_stage(self):
        """Set up the group stage """
        if len(self.teams) == 8:
            #Create two groups of four teams each
            group_a = self.teams[:4]
            group_b = self.teams[4:]
            #Create games for group A
            self.set_group(group_a, "Group A")
            #Create games for group B
            self.set_group(group_b, "Group B")


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
    tournament.set_group_stage()
    print(tournament.groups['Group A'].games)
    print(tournament.groups['Group B'].games)
    #print(tournament)
                
