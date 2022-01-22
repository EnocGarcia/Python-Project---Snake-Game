from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)
