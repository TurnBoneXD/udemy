from turtle import Turtle,Screen, color, turtles
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make our bet",prompt="Which turtle will win the race?")
colors = ["red","orange","yellow","green","blue","purple"]
y_position = [-75,-45,-15,15,45,75]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-238,y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've win! The {winner} turtle is the winner!")
            else:
                print(f"You've lose! The {winner} turtle is the winner!")
            

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


    
    

screen.exitonclick()