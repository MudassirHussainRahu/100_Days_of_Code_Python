from prettytable import PrettyTable

class MenuItem:
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee":coffee
        }

    def __str__(self):
        table = PrettyTable()
        table.align = "l"
        table.add_column("Name", [self.name])
        table.add_column("Cost", [self.cost])
        ing = list(self.ingredients.keys())
        quan = list(self.ingredients.values())
        quan = [ str(q) for q in quan ]
        table.add_column("Ingredients", ["|".join(ing)])
        table.add_column("Quantities", ["|".join(quan)])
        print(table)
        return f"{self.name}"

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("latte", 2.5, 200, 150, 24),
            MenuItem("espresso", 1.5, 50, 0, 18),
            MenuItem("cappuccino", 3, 250, 50, 24)
        ]

    def get_items(self):
        items = ""
        for i in self.menu:
            items = items+i.name+"/"
        return items
    
    def find_drinks(self, order_name):
        for i in self.menu:
            if i.name == order_name:
                return i
        return None
    
