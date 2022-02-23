import turtle
from turtle import Turtle, Screen
import random
screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the bet, Enter a color: ')
colors = ["red", "orange", "blue", "purple", "green", "yellow"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for num in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[num])
    new_turtle.goto(x=-230, y=y_positions[num])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!. The {winning_color} color is the winner!")
            else:
                print(f"You've lost!. The {winning_color} color is the winner!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)





screen.exitonclick()
