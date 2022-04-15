from turtle import Turtle,Screen

# w = fowards
# s = backwards
# a = counter clockwise
# d = clockwise
# c = clear

tim = Turtle()
screen = Screen()

def move_fowards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    tim.left(10)

def clockwise():
    tim.right(10)

def clear():
    tim.setpos(0,0)
    tim.clear()
    tim.setheading(0)

screen.listen()
screen.onkey(key="w",fun=move_fowards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clear)
screen.exitonclick()