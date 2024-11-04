import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_existing_player(self):
        vastaus = self.stats.search("Semenko")

        self.assertAlmostEqual(vastaus.name, "Semenko")

    def test_search_doesnt_return_non_existing_players(self):
        vastaus = self.stats.search("Ville")

        self.assertAlmostEqual(vastaus, None)

    def test_team_returns_list_of_players(self):
        vastaus = self.stats.team("EDM")

        names = [player.name for player in vastaus]

        self.assertListEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_top_works_points(self):
        vastaus = self.stats.top(3, SortBy.POINTS)

        names = [player.name for player in vastaus]

        self.assertListEqual(names, ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_works_goals(self):
        vastaus = self.stats.top(3, SortBy.GOALS)

        names = [player.name for player in vastaus]

        self.assertListEqual(names, ["Lemieux", "Yzerman", "Kurri"])

    def test_top_works_assists(self):
        vastaus = self.stats.top(3, SortBy.ASSISTS)

        names = [player.name for player in vastaus]

        self.assertListEqual(names, ["Gretzky", "Yzerman", "Lemieux"])


    