from menu import Menu, MenuItem
from coffeemaker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
menu_items = menu.get_items()

coffee_maker = CoffeeMaker(300,200,100)

money_machine = MoneyMachine()

while True:
    option = input(f"What would you like? ({menu_items}):")

    if option == "off":
        print("Turning Off!")
        break   
    elif option == "report":
        coffee_maker.report()
        print(f"Profit is {money_machine.profit}")
    elif option in  menu_items:
        drink = menu.find_drinks(option)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            print("Fail")
    else:
        print("Invlid Input!")
        
