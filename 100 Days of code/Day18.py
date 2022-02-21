import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("coral")
turtle.colormode(255)

# To create a square shape
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# for i in range(10):
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)

# colors = ["red", "orange", "purple", "green", "blue", "cyan", "green", "coral", "pink", "brown"]

# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shapes(shape_side_n)


# To create a random walk
# tim.width(15)
tim.speed('fastest')
#
# directions = [0, 90, 180, 270]


# creating completely random colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb
#
#
# for i in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# Making a spirograph
def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
