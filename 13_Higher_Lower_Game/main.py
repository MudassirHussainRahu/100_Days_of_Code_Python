import random
import os

from game_art import logo, vs
from game_data import data

score = 0

def clear():
    os.system("cls")


choice_1 = None
choice_2 = None


while 1:
    clear()
    print(logo)
    if choice_1 == None:
        choice_1 = random.choice(data)

    choice_2 = random.choice(data)

    while choice_1 == choice_2:
        choice_2 = random.choice(data)
    
    print("Score is ", score)
    print("Name:",choice_1["name"]," Followers:", choice_1["follower_count"])
    print(vs)
    print("Name:",choice_2["name"]," Followers: ?")

    choice = input(f"{choice_2["name"]} has higher or lower followers? ")

    if choice.lower() == "higher":
        if choice_2["follower_count"] > choice_1["follower_count"]:
            score += 1
            choice_1 = choice_2
        elif choice_2["follower_count"] == choice_1["follower_count"]:
            score += 1
            choice_1 = choice_2
        else:
            print("Wrong!")
            print("Your score is", score)
            break
    
    elif choice.lower() == "lower":
        if choice_2["follower_count"] < choice_1["follower_count"]:
            score += 1
            choice_1 = choice_2
        elif choice_2["follower_count"] == choice_1["follower_count"]:
            score += 1
            choice_1 = choice_2
        else:
            print("Wrong!")
            print("Your score is", score)
            break

    else:
        print("Invalid Choice!")
    







