from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Choose Turle", prompt="Enter a color:")
# print(user_choice)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
x = -240
y = +185

for color in colors:
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.shapesize(1)
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x, y)
    y -= 70
    turtles.append(new_turtle)

if user_choice:
    is_race_on = True

winner_color = None

while is_race_on:
    for turtle in turtles:
        rand_distance = randint(0,10)
        turtle.forward(rand_distance)
        (x,y) = turtle.pos()
        if x >= 240:
            is_race_on = False
            winner_color = turtle.pencolor()
            break

if user_choice in colors:
    if user_choice.lower() == winner_color:
        print("Congratulations YOU WON!")
    else:
        print(f"You Lost. {winner_color} turtle is winner")
else:
    print(f"Invalid Choice!. {winner_color} turtle is winner")
screen.exitonclick()