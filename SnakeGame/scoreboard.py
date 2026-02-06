import os
from turtle import Screen, Turtle

screen = Screen()
ALIGNMENT = "Center"
FONT = ("Courier", 22, "normal")

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HIGH_SCORE_FILE = os.path.join(SCRIPT_DIR, "high-score.txt")


class ScoreBoard(Turtle):
    def __init__(self):
        self.count = 0
        self.high_count = 0
        
        # Read high score if file exists, otherwise start at 0
        if os.path.exists(HIGH_SCORE_FILE):
            with open(HIGH_SCORE_FILE) as data:
                self.high_count = int(data.read())

        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.write(
            f"Score :: {self.count} | High Score :: {self.high_count}",
            align=ALIGNMENT,
            font=FONT,
        )

    def update(self):
        self.clear()
        self.write(
            f"Score :: {self.count} | High Score :: {self.high_count}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.count > self.high_count:
            self.high_count = self.count

            with open(HIGH_SCORE_FILE, "w") as h:
                h.write(f"{self.high_count}")

        self.count = 0

    def increase_score(self):
        self.hideturtle()
        self.count += 1
        self.update()

