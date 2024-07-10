from turtle import Turtle

FONT = ("Arial", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()

        with open("highscore.txt") as score:
            self.h_score = score.read()
            self.h_score=int(self.h_score)

        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"score = {self.score}  High score{self.h_score}", move=False, align="center", font=FONT)


    def increase_high_score(self):
        if self.score > self.h_score:
            self.h_score=self.score
            with open("highscore.txt", mode="w") as score:
                score.write(f"{self.h_score}")
        self.score=0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()




