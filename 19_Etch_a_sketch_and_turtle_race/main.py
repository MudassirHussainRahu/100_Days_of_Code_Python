# Python higher order function
#   a function that can work with other function ( can take fucntions as input)
# Turtle Event Listeners

# Object State and Instances




from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)



screen.exitonclick()