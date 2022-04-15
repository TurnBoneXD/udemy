import turtle as t
import random 

color = ["CadetBLue","DarkOrchid","DarkRed","aquamarine",
"coral","DarkGreen","gold1","magenta"]



tim = t.Turtle()
tim.shape("classic")
tim.pensize(5)
tim.speed("fastest")


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color



direction = [0,90,180,270]

while True:
    tim.color(random_color())
    tim.setheading(random.choice(direction))
    tim.forward(25)






    





screen = t.Screen()
screen.exitonclick()