"""
Password Generator
Instructions
The program will ask:
How many letters would you like in your password?
How many symbols would you like?
How many numbers would you like?
The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.
Easy Version (Step 1)
Generate the password in sequence. If the user wants
    4 letters
    2 symbols and
    3 numbers
then the password might look like this:
fgdx$*924
You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.
Hard Version (Step 2)
When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:
x$d24g*f9
And every time you generate a password, the positions of the symbols, numbers, and letters are different.
"""
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def easy(ltr, syb, num):

    lettersPart = []
    symbolsPart = []
    numberPart = []

    for n in range(0, ltr):
        p = random.randint(0, len(letters)-1)
        lettersPart.append(letters[p])

    for n in range(0, syb):
        p = random.randint(0, len(symbols)-1)
        symbolsPart.append(symbols[p])

    for n in range(0, num):
        p = random.randint(0, len(numbers)-1)
        lettersPart.append(numbers[p])

    lettersPart = ''.join(lettersPart)
    symbolsPart = ''.join(symbolsPart)
    numberPart = ''.join(numberPart)
    return lettersPart+symbolsPart+numberPart

def hard(ltr, syb, num):
    t = [letters, symbols, numbers]
    symbolCount = 0
    numberCount = 0
    password = [None for i in range(0, ltr+syb+num)]
    
    for i in range(0, ltr):
        l = letters[random.randint(0, len(letters)-1)]
        p = random.randint(0, len(password)-1)
        password[p] = l

    while 1:
        if symbolCount == syb:
            break
        s = symbols[random.randint(0, len(symbols)-1)]
        p = random.randint(0, len(password)-1)
        while 1:
            if password[p] == None:
                break
            else:
                p = random.randint(0, len(password)-1)
        password[p] = s
        symbolCount += 1
    while 1:
        if numberCount == num:
            break
        n = numbers[random.randint(0, len(numbers)-1)]
        p = random.randint(0, len(password)-1)
        while 1:
            if password[p] == None:
                break
            else:
                p = random.randint(0, len(password)-1)
        password[p] = n
        numberCount += 1    
    password = ''.join(password)
    return password


print('Welcome to Password Generator')

num_letters = int(input('How many letters would you like in your password?\n'))
num_symbols = int(input('How many symbols would you like in your password?\n'))
num_numbers = int(input('How many numbers would you like in your password?\n'))

print(easy(num_letters, num_symbols, num_numbers))
print(hard(num_letters, num_symbols, num_numbers))






