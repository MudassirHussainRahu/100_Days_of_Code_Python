from prettytable import PrettyTable

class CoffeeMaker:
    def __init__(self, water, milk, coffee):
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

    def report(self):
        table = PrettyTable()
        table.add_column("Ingredient", ["Water", "Milk", "Coffee"])
        table.add_column("Qunatity", list(self.ingredients.values()))
        table.align = "l"
        print(table)

    def is_resource_sufficient(self, drink):
        sufficient = True
        for ing in drink.ingredients.keys():
            if drink.ingredients[ing] > self.ingredients[ing]:
                print(f"Sorry there is not enough {ing}.")
                sufficient = False
                break
        return sufficient
    
    def make_coffee(self, order):
        for ing in order.ingredients.keys():
            self.ingredients[ing] -= order.ingredients[ing]

        print(f"Here is your {order.name}. Enjoy!")
