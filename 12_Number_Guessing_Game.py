# Scope: Local( within block of code ) and Global (available in entire code)
# global keyword

import random

print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1,100)

difficulty = input("Type 'easy' or 'hard': ")

number_of_guesses = 0

if difficulty.lower() == "easy":
    number_of_guesses = 10
elif difficulty.lower() == "hard":
    number_of_guesses = 5
else:
    print("Invalid Choice")

while number_of_guesses > 0:
    print(f"You have {number_of_guesses} attempts remaining.")
    guess = int(input("Enter guess:"))
    if guess == number:
        print("You Won!")
        break

    if guess < number:
        print("Too Low.")
    
    if guess > number:
        print("Too High.")

    number_of_guesses -= 1

if number_of_guesses == 0:
    print("You Lose!")

print("End Game!")
