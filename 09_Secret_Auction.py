import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
Bids = {}


def enterInformation():
    name = input('What is your name? : ')
    bid = input('What is your bid? : ')
    if name.lower() in Bids.keys():
        print('You have already bidded.')
    else:
        if bid.isnumeric():
            Bids[name.lower()] = float(bid)
        else:
            print('Invalid Bid: Bid must be numerical value.')

def check():
    s = input('Are there any other bidders? Type \'yes\' or \'no\': ')
    if s.lower() == 'yes':
        return True
    elif s.lower() == 'no':
        return False
    else:
        print('Invalid Input')
        return False

def clear():
    os.system('cls')

def winnerIs():
    names = list(Bids.keys())
    winner = names[0]
    bid = Bids[winner]
    
    for name in names:
        if Bids[name] > bid:
            winner = name
            bid = Bids[name]
        else:
            continue

    print(f'The winner is {winner} with a bid of ${bid}')



print(logo)
print('Welcome to Blind Auction!')

while 1:
    enterInformation()
    if not(check()):
        clear()
        break
    else:
        clear()
        continue

winnerIs()
