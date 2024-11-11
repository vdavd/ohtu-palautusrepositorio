class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
    
    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals} + {self.assists} = {self.goals+self.assists}"