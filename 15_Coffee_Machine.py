MENU = {
    "espresso":{
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
profit = 0

def report():
    print(f"---------Resources---------------")
    print(f"Water: {resources['water']}ml.")
    print(f"Milk: {resources['milk']}ml.")
    print(f"Coffee: {resources['coffee']}g.")
    print(f"Money: ${profit}")

def check_resources(choice):
    ingredients = MENU[choice]["ingredients"]
    enough_resources = True
    for r in ingredients.keys():
        # print(ingredients[r] , resources[r])
        if ingredients[r] > resources[r]:
            enough_resources = False
            print(f"Sorry there is not enough {r}")
            break
    return enough_resources

def calculate_money(q,d,n,p):
    return round(0.25*q + 0.1*d + 0.05*n + 0.01*p,2)

def sufficiant_amount(choice, money):
    cost = MENU[choice]["cost"]
    if money < cost:
        return False
    return True

def deplete_resources(choice):
    for r in MENU[choice]["ingredients"].keys():
        resources[r] -=  MENU[choice]["ingredients"][r]


def coffee():
    print("Welcome to Coffee Machine!")

    while True:
        choice = input( "What would you like? (espresso/latte/cappuccino):")
        if choice == "off":
            report()
            print("Shutting Off.")
            break

        elif choice == "report":
            report()
        elif choice in MENU.keys():
            # print(choice)
            if check_resources(choice):
                try:
                    quarters = int(input("Enter Quarters:"))
                    dimes = int(input("Enter Dimes:"))
                    nickels = int(input("Enter Nickels:"))
                    pennies = int(input("Enter Pennies:"))
                    money = calculate_money(quarters, dimes, nickels, pennies)
                    # print(money)
                    if sufficiant_amount(choice, money):
                        cost = MENU[choice]["cost"]
                        change = round(money - cost,2)
                        profit += cost
                        deplete_resources(choice)
                        if change > 0:
                            print(f"Here is ${change} dollars in change.")
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                except:
                    print("Invalid Coins.")
        else:
            print("Invalid Input.")


coffee()