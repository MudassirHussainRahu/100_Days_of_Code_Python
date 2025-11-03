import colorgram

from turtle import Turtle, Screen

from random import randrange

colors = colorgram.extract("image.jpg", 30)

color = []
for clr in colors:
    color.append((clr.rgb[0],clr.rgb[1],clr.rgb[2]))
    
print(color)


t = Turtle()
screen = Screen()
screen.colormode(255)
# screen.addshape(400,400)
t.hideturtle()
t.penup()


t.setx(-200)
t.sety(-200)


# t.dot(20, "blue")


for j in range(10):
    for i in range(10):
        index = randrange(len(color))
        c = color[index]
        t.color(c)
        t.dot(20)
        t.forward(50)

    (x,y) = t.position()
    # print(x,y)
    t.setx(-200)
    t.sety(y+50)

screen.exitonclick()

