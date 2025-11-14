from turtle import Turtle, Screen
import pandas as pd


data = pd.read_csv("50_states.csv")

# print(data.head(10))

# print(data.iloc[0]["x"])

# (x,y) = data.iloc[0]["x"], data.iloc[0]["y"]


states = data["state"].to_list()
print(states)

guessed_states = []

screen = Screen()
screen.title("United States Game")
turtle = Turtle()
turtle.penup()
turtle.hideturtle()

s = 0
score = Turtle()
score.penup()
score.color("black")
score.hideturtle()
score.goto(0,250)
score.write(f"States Guessed:{s}")

guess = Turtle()
guess.penup()
guess.color("black")
guess.hideturtle()
guess.goto(-250,250)
g = "No"
guess.write(f"{g} Guess!")



screen.bgpic("blank_states_img.gif")

game_is_on = True

while game_is_on:
    state = screen.textinput("State Name", "Enter name of the state:")
    if state in states:
        x = data[ data["state"] == state ].iloc[0]["x"]
        y = data[ data["state"] == state ].iloc[0]["y"]
        turtle.goto(x,y)
        turtle.write(f"{state}")
        score.clear()
        s += 1
        score.write(f"States Guessed:{s}")
        g = "Correct"
        guess.clear()
        guess.write(f"{g} Guess!")
        guessed_states.append(state)
        states.remove(state)
    elif state.lower() == "exit":
        print("Exiting")
        game_is_on = False
    elif state in guessed_states:
        guess.clear()
        guess.write(f"Guessed Already")
    else:
        g = "Wrong"
        guess.clear()
        guess.write(f"{g} Guess!")
    
# draw(x,y)


screen.exitonclick()

# print(state)

# print(data[ data["state"] == "alabama".capitalize() ].iloc[0]["x"])

missed_states = pd.DataFrame(states)
missed_states.to_csv("missed_states.csv")