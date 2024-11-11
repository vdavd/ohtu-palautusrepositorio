from player import Player

class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality: str):
            
        def nat_player_func(player, nationality):
            if player.nationality == nationality:
                return True
            else:
                return False
            
        nat_players = filter(nat_player_func(nationality), self.players)

        ordered_players = sorted(nat_players, key=lambda player: player.goals + player.assists, reverse=True)

        return ordered_players


                