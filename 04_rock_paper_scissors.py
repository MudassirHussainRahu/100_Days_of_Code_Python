import random

rock = f'''
    -----
___'    __)
        (___)
        (___)
        (__)
----.__(__)
'''

paper = f'''
    -------
___'    ____)____
            ______)
            ________)
        (_________)
----.__(_________)
'''



scissors = f'''
    -------
___'    ____)____
            ______)
            ________)
        (____)
----.__(____)
'''

rockPaperScissors = [rock, paper, scissors]

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
computerChoice = random.randint(0,2)

if choice < len(rockPaperScissors):
    print(f'Your Choice {choice}')
    print(rockPaperScissors[choice])
    print(f'Computer chose:')
    print(rockPaperScissors[computerChoice])


if choice == 0:
    if computerChoice == 0:
        print('Draw')
    elif computerChoice ==1:
        print('You lose')
    else:
        print('You Won')
elif choice ==1:
    if computerChoice == 0:
        print('You Won')
    elif computerChoice ==1:
        print('Draw')
    else:
        print('You lose')
elif choice == 2:
    if computerChoice == 0:
        print('You lose')
    elif computerChoice ==1:
        print('You won')
    else:
        print('Draw')
else:
    print("Invalid Input You lose.")
