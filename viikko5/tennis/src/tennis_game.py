class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score1 = 0
        self.score2 = 0
        self.score_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.score1 += 1
        else:
            self.score2 += 1

    def get_score(self):
        score = ""
        temp_score = 0

        if self.even_score():
            return self.even_score()

        elif self.score_over_4():
            return self.score_over_4()

        else:
            return self.uneven_score()

    
    def even_score(self):
        if self.score1 == self.score2:
            if self.score1 >= 3:
                return "Deuce"
            else:
                return self.score_names[self.score1] + "-All"
        else:
            score = False
        
        return score

    def score_over_4(self):
        if self.score1 >= 4 or self.score2 >= 4:
            difference = self.score1 - self. score2

            if difference == 1:
                score = "Advantage player1"
            elif difference == -1:
                score = "Advantage player2"
            elif difference >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"

        else:
            score = False

        return score

    def uneven_score(self):
        return self.score_names[self.score1] + "-" + self.score_names[self.score2]

