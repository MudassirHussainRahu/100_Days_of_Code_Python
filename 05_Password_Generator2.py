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

def easy(num_letters, num_symbols, num_numbers):
    password = ''

    for char in range(1, num_letters+1):
        password += random.choice(letters)

    for symbol in range(1, num_symbols+1):
        password += random.choice(symbols)
    
    for number in range(1, num_numbers+1):
        password += random.choice(numbers)

    return password


def hard(num_letters, num_symbols, num_numbers):
    password = []
    for char in range(1, num_letters+1):
        password.append(random.choice(letters))

    for symbol in range(1, num_symbols+1):
        password.append(random.choice(symbols))

    for number in range(1, num_numbers+1):
        password.append(random.choice(numbers))

    random.shuffle(password)
    password = ''.join(password)
    return password





letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print('Welcome to Password Generator')

num_letters = int(input('How many letters would you like in your password?\n'))
num_symbols = int(input('How many symbols would you like in your password?\n'))
num_numbers = int(input('How many numbers would you like in your password?\n'))

print(hard(num_letters, num_symbols, num_numbers))

