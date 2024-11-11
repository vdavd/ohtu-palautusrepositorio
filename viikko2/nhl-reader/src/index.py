
from playerStats import PlayerStats
from playerReader import PlayerReader

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader.get_players())
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()