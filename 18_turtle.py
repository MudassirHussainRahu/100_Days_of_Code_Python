from turtle import Turtle, Screen
from random import random, choice, randint

import heroes

# creating turtle object
t = Turtle()

#creating screen object
screen = Screen()
screen.title("Object Oriented turtle demo")
screen.bgcolor("white")

# setting color of turtle
t.color("#98FB98")

    
# calling function
# draw_square()

def draw_dotted_line():
    for i in range(20):
        if i % 2 == 0:
            t.down()
        else:
            t.up()
        t.forward(10)


# draw_dotted_line()


list_of_colors = ["#98FB98", "#7DF4E4", "#890505", "#EA4444", "#0A1577", "#E498FB", "#7B086C", "#426A6C"]

def draw_triangle():
    t.down()
    t.color(list_of_colors[0])
    for i in range(3):
        t.forward(100)
        t.right(120)
    


def draw_square():
    t.down()
    t.color(list_of_colors[1])
    for _ in range(4):
        t.forward(100)
        t.right(90)

def draw_pentagon():
    t.down()
    t.color(list_of_colors[2])
    for _ in range(5):
        t.forward(100)
        t.right(72)

def draw_hexagon():
    t.down()
    t.color(list_of_colors[3])
    for _ in range(6):
        t.forward(100)
        t.right(60)

def draw_heptagon():
    t.down()
    t.color(list_of_colors[4])
    for _ in range(7):
        t.forward(100)
        t.right(51.4285)

def draw_octagon():
    t.down()
    t.color(list_of_colors[5])
    for _ in range(8):
        t.forward(100)
        t.right(45)

def draw_nonagon():
    t.down()
    t.color(list_of_colors[6])
    for _ in range(9):
        t.forward(100)
        t.right(40)

def draw_decagon():
    t.down()
    t.color(list_of_colors[7])
    for _ in range(10):
        t.forward(100)
        t.right(36)



# draw_triangle()
# draw_square()
# draw_pentagon()
# draw_hexagon()
# draw_heptagon()
# draw_octagon()
# draw_nonagon()
# draw_decagon()


def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.left(angle)

# for i in range(3,11):
#     draw_shape(i)


def random_color():
    r = randint(0,255)/255
    g = randint(0,255)/255
    b = randint(0,255)/255
    random_clr = (r,g,b)
    return tuple(random_clr)

# t.width(10)
# angles = [0, 90, 180, 270, 360]
# t.speed("fastest")

# for _ in range(200):
#     rclr = random_color()
#     t.pencolor(rclr)
#     t.forward(30)
#     t.setheading(choice(angles))


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)


# draw_spirograph(5)



# for i in range(0,500,10):   
#     t.circle(100)
#     t.left(t.heading() + i)



screen.exitonclick()
