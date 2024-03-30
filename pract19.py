import os
import time
import random
from ball import Ball
from scoreboard import Scoreboard


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def hit_ball(self, ball):
        return self.x == ball.x and self.y <= ball.y < self.y + 3


def draw(screen, ball, player_paddle, opponent_paddle, scoreboard, width, height):
    os.system("cls" if os.name == "nt" else "clear")
    for _ in range(width):
        print("-", end="")
    print()

    for row in range(height):
        for col in range(width):
            if col == 0 or col == width - 1:
                print("|", end="")
            elif ball.x == col and ball.y == row:
                print("O", end="")
            elif player_paddle.x == col and (
                player_paddle.y <= row < player_paddle.y + 3
            ):
                print("|", end="")
            elif opponent_paddle.x == col and (
                opponent_paddle.y <= row < opponent_paddle.y + 3
            ):
                print("|", end="")
            else:
                print(" ", end="")
        print()

    for _ in range(width):
        print("-", end="")
    print()

    scoreboard.display_scores()


def main():
    width = 30
    height = 20
    screen = [[" "] * width for _ in range(height)]

    ball = Ball(width // 2, height // 2, 1, 1)
    player_paddle = Paddle(1, height // 2 - 1)
    opponent_paddle = Paddle(width - 2, height // 2 - 1)
    scoreboard = Scoreboard()

    running = True
    while running:
        draw(screen, ball, player_paddle, opponent_paddle, scoreboard, width, height)

        ball.move()
        ball.bounce_off_wall(width, height)

        if ball.x == player_paddle.x + 1:
            if player_paddle.hit_ball(ball):
                ball.bounce_off_paddle()
            else:
                scoreboard.increase_opponent_score()
                ball.reset_position(width // 2, height // 2, 1, 1)
                time.sleep(1)

        if ball.x == opponent_paddle.x - 1:
            if opponent_paddle.hit_ball(ball):
                ball.bounce_off_paddle()
            else:
                scoreboard.increase_player_score()
                ball.reset_position(width // 2, height // 2, -1, -1)
                time.sleep(1)

        if ball.y == 0 or ball.y == height - 1:
            ball.speed_y *= -1

        ball.move()

        if ball.x == 0 or ball.x == width - 1:
            ball.speed_x *= -1

        if ball.speed_x < 0:
            opponent_paddle.y = ball.y - 1
        else:
            opponent_paddle.y = random.randint(0, height - 3)

        for event in input():
            if event == "w":
                player_paddle.move_up()
            elif event == "s":
                player_paddle.move_down()

            if event == "q":
                running = False

        time.sleep(0.03)

    os.system("cls" if os.name == "nt" else "clear")
    print("Game Over!")
    print(
        f"Final Scores: Player - {scoreboard.player_score}, Opponent - {scoreboard.opponent_score}"
    )


if __name__ == "__main__":
    main()
