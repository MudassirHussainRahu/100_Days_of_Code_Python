
# Fix the bugs

# number = int(input("Which number do you want to check?"))

# if number % 2 = 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

number = int(input("Which number do you want to check?"))
if number%2==0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# year = input("Which year do you want to check?")

# if year % 4 == 0:
#     if year %100 == 0:
#         if year % 400 == 0:
#             print("Leap Year")
#         else:
#             print("Not leap year")
#     else:
#         print("leap year")
# else:
#     print("Not leap year")

year = int(input("Which year do you want to check?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year.")
        else:
            print("Not Leap Year.")
    else:
        print("Leap Year.")
else:
    print("Not Leap Year.")
# for number in range(1,101):
#     if number%3 == 0 or number%5==0:
#         print("FizzBuzz")
#     if number % 3 == 0:
#         print("Fizz")
#     if number % 5 == 0:
#         print("Bizz")
#     else:
#         print([number])

for number in range(1,101):
    if number%3 == 0 and number%5 == 0:
        print("FizzBuzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else:
        print(number)
