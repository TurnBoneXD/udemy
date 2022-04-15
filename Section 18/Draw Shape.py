import turtle as t

color = ["CadetBLue","DarkOrchid","DarkRed","aquamarine",
"coral","DarkGreen","gold1","magenta"]

tim = t.Turtle()
tim.shape("classic")

for num in range(8):
    tim.color(color[num])
    num += 3
    for round in range(num):
        tim.forward(100)
        tim.right(360/num)





    





screen = t.Screen()
screen.exitonclick()