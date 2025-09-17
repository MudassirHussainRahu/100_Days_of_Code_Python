############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Game Rule #########################
## Blackjack or 21
## Add cards upto 21 
## You lose if cards add up is greater than 21
## Ace can either count as 1 or 11 (  )
## dealer must take another card if its score is less than 17


import os
import random


logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards)> 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def black_jack():

    user_cards = []
    computer_cards = []
    is_game_over = False
    print(logo)

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not (is_game_over):
        print("User Cards:", user_cards)
        print("User Score:", calculate_scores(user_cards))
        print("Computer Cards:", computer_cards[0])
        
        if calculate_scores(user_cards) == 0:
            print("Black Jack!")
            print("User Wins!")
            is_game_over = True

        elif calculate_scores(user_cards)>21:
            print("Computer Wins!")
            is_game_over = True

        else:
            op = input("H for Hit, S for Stand:")

            if op.lower() == "s":

                user_score = calculate_scores(user_cards)
                computer_score = calculate_scores(computer_cards)
                print("Computer Cards:", computer_cards)
                print("Computer Score:", computer_score)
                
                while computer_score < 17 and computer_score != 0:

                    print(f"Computer Score: {computer_score} < 17, So Computer Draws Card!")
                    computer_cards.append(deal_card())
                    computer_score = calculate_scores(computer_cards)
                    print("Computer Cards:", computer_cards)
                    print("Computer Score:", computer_score)

                if computer_score == 0:
                    print("Black Jack!")
                    print("Dealer Wins!")

                if computer_score > 21:
                    print("User Wins!")
                
                if computer_score > 0 and computer_score < 21:
                    if computer_score == user_score:
                        print("Draw!")
                    elif computer_score > user_score:
                        print("Computer Wins!")
                    else:
                        print("User Wins!")

                is_game_over = True

            if op.lower() == "h":

                user_cards.append(deal_card())
    print("Game Ended!")


clear = lambda: os.system('cls')
while True:
    option = input("Enter P for play and E for exit.")
    if option.lower() == "p":
        clear()
        black_jack()

    if option.lower() == "e":
        clear()
        break

    



