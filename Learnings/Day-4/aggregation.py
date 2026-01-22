class player:
    def __init__(self, name):
        self.name = name
        
class Team:
    def __init__(self,players):
        self.players = players #players created elsewhere
        
players = [player("A"), player("B")]
team = Team(players)

for player in team.players:
    print(player.name)

