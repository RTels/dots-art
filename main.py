import turtle
from turtle import Turtle, Screen
import random
colors = [(0, 0, 0), (246, 245, 241), (136, 78, 52), (26, 85, 158), (218, 134, 59), (184, 18, 59), (137, 190, 3),
          (150, 193, 205), (1, 144, 74), (222, 41, 97), (246, 145, 163), (249, 92, 13), (150, 42, 110)]

screen = Screen()
screen.setup(width=800, height=800)
turtle.colormode(255)
timmy = turtle.Turtle()
timmy.hideturtle()
timmy.speed("fastest")
timmy.penup()
timmy.setheading(255)
timmy.forward(370)
timmy.setheading(0)

dots_number = 100
def change_pos():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)


for dot_count in range(1, dots_number+1):
    timmy.dot(20, random.choice(colors))
    timmy.forward(50)
    if dot_count % 10 == 0:
        change_pos()




















screen.exitonclick()












