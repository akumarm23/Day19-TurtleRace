# Turtle Race Python Code v0.1

# Import necessary modules
from turtle import Turtle, Screen
import random

# Set up the initial state of the race
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")

# Get user's bet on the winning turtle color
user_bet = screen.textinput(title="Make your BET", prompt="Which Color Turtle will win the race? :\norange\nyellow\nred\nfuchsia\nlime\naqua")
colors = ["orange", "yellow", "red", "fuchsia", "lime", "aqua"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create turtles and set their initial positions
for index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[index])
    turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(turtle)

# If the user has made a bet, start the race
if user_bet:
    is_race_on = True

# Simulate the race
while is_race_on:
    for turtle in all_turtles:
        # Check if a turtle has reached the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            # Announce the result based on user's bet
            if win_color == user_bet:
                print("Congratulations! You WON!!! Enjoy your victory!\n")
            else:
                print(f"You LOST! Better luck next time. The {win_color} turtle WON.\n")
        # Move each turtle a random distance forward
        distance = random.randint(0, 10)
        turtle.forward(distance)

# Close the screen on click
screen.exitonclick()

# END OF CODE
