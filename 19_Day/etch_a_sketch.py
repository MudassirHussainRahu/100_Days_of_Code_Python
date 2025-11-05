from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def screen_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def tim_forward():
   tim.forward(10)


def tim_backward():
    tim.backward(10)


def left():
    heading = tim.heading() + 10
    tim.setheading(heading)

def right():
    heading = tim.heading() - 10
    tim.setheading(heading)



screen.listen()
screen.onkey(key="w", fun=tim_forward)
screen.onkey(key="s", fun=tim_backward)
screen.onkey(key="d", fun=left)
screen.onkey(key="a", fun=right)
screen.onkey(key="c", fun=screen_clear)

screen.exitonclick()