from turtle import Turtle

FONT = ('Times New Roman', 24, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)

    # Display the starting scoreboard
    def start_scoreboard(self):
        self.goto(-50,270)
        #align='center'
        self.write(arg=f"Score: {self.score}",  font=FONT)

    # Increase and update the scoreboard
    def increase_scoreboard(self):
        self.clear()
        self.score += 1
        self.start_scoreboard()

    # Display the "Game Over" message
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align='center', font=FONT)
        self.goto(-100, -50)
        self.write("Restart? Click anywhere.", font=FONT)

    # Reset the scoreboard
    def reset(self):
        self.clear()  # Clear the previous score
        self.score = 0  # Reset score to 0
        self.start_scoreboard()  # Display the updated scoreboard
