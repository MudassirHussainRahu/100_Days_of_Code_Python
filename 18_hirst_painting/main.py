import colorgram  # Import colorgram to extract colors from images

from turtle import Turtle, Screen  # Import Turtle graphics modules

from random import randrange  # Import randrange for picking random colors

# Extract 30 colors from the image "image.jpg"
colors = colorgram.extract("image.jpg", 30)

color = []
# Convert the extracted colors to a list of RGB tuples
for clr in colors:
    color.append((clr.rgb[0], clr.rgb[1], clr.rgb[2]))
    
print(color)  # Print the list of extracted colors


t = Turtle()  # Create a new Turtle object
screen = Screen()  # Create a new Screen object
screen.colormode(255)  # Set the color mode to use RGB values up to 255
# screen.addshape(400,400)  # (Commented out) Would add a custom shape if needed
t.hideturtle()  # Hide the turtle icon
t.penup()  # Lift the pen to avoid drawing lines between dots


# Set initial starting position for drawing
t.setx(-200)
t.sety(-200)


# t.dot(20, "blue")  # (Commented out) Example of drawing a single blue dot


# Draw a 10x10 grid of colored dots
for j in range(10):  # For each row
    for i in range(10):  # For each column in the row
        index = randrange(len(color))  # Choose a random color index
        c = color[index]  # Get the corresponding color
        t.color(c)  # Set the turtle color to the chosen color
        t.dot(20)  # Draw a dot of diameter 20
        t.forward(50)  # Move forward to position for the next dot

    (x, y) = t.position()  # Get the current position
    # print(x,y)  # (Optional) print out the current coordinates
    t.setx(-200)  # Move turtle back to the start of the row
    t.sety(y + 50)  # Move turtle up to start a new row

screen.exitonclick()  # Keep the window open until clicked
