from flask import Flask
import random


app = Flask(__name__)
random_number = random.randint(0, 9)
print(random_number)


@app.route("/")
def home_page():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGUzcDZuczJhcGpkbThhY3o5eWlqcnM3NDRuOWdweWVuMnFmdjZ5eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kyLYXonQYYfwYDIeZl/giphy.webp" width=200>'
    )


@app.route("/<int:guess>")
def user_guess(guess):
    if guess < random_number:
        return (
            '<h1 style="color: green">Too low, try again.</h1>'
            '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExOG1tdjMybWM4dWkwZnl2MmF0OHVlZ2NwaXI5ZmM1MTM4NWttbXMyciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3drHXsi8EwBK7dEqCF/giphy.webp" width=200>'
        )
    elif guess == random_number:
        return (
            '<h1 style="color: green">Correct, you won!</h1>'
            '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHNsNmI0a2FzajFyMDQxcGc3NmdpY2RyMnQyOW4zZHV5bTJ1dWV2dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o85xJMBIk9mmyemvS/giphy.webp" width=200>'
        )
    else:
        return (
            '<h1 style="color: green">Too high, try again.</h1>'
            '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHBjN25tY2VsaDI1c252YWd1enUzaHo2dXphMXl6bGo4b2JhOTdvcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KZVILnTgM8bAs/giphy.webp" width=200>'
        )


if __name__ == "__main__":
    app.run(debug=True)
