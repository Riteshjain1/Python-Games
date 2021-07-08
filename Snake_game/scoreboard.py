from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        with open("data.txt") as file:
            contents = file.read()
            arr = contents.split(" ")
        self.high_score = int(arr[2])
        self.hideturtle()
        self.goto(0, 270)
        self.rewrite()

    def increase_score(self):
        self.score += 1
        self.rewrite()

    def rewrite(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def res(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"high score {self.high_score}")
        self.score = 0
        self.rewrite()


    # def end_game(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over!", align=ALIGN, font=FONT)