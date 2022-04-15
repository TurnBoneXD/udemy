import turtle as t
import random 

tim = t.Turtle()
tim.shape("classic")
tim.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color


for _ in range(300):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + 2)






screen = t.Screen()
screen.exitonclick()