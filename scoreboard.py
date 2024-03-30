class Scoreboard:
    def __init__(self):
        self.player_score = 0
        self.opponent_score = 0

    def increase_player_score(self):
        self.player_score += 1

    def increase_opponent_score(self):
        self.opponent_score += 1

    def display_scores(self):
        print(f"Player: {self.player_score} | Opponent: {self.opponent_score}")

    def reset_scores(self):
        self.player_score = 0
        self.opponent_score = 0
