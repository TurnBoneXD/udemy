from tkinter import Y
import colorgram
import turtle
import random

rgb_color = []
turtle.colormode(255)

colors = colorgram.extract('image.jpg', 20)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_color.append(new_color)

tim = turtle.Turtle()
tim.shape("classic")

x = 0
y = 0
for _ in range(10):
    turtle.penup()
    turtle.setpos(x,y)
    for _ in range(10):
        turtle.setpos(x,y)
        turtle.pendown()
        turtle.dot(20,random.choice(rgb_color))
        turtle.penup()
        x += 50
    x = 0
    y += 50


screen = turtle.Screen()
screen.exitonclick()