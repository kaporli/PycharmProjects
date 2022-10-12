penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coffee_machine(name, water, coffee, cost):
    wants_coffee = True
    old_key = "None"
    while wants_coffee is True:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
        for key in MENU:
            if coffee_type == key:
                cost = MENU[key]["cost"]
                print(f"Your coffee costs {cost}$.")
                print("Please insert coins.")
                quarters = int(input("how many quarters?: "))
                dimes = int(input("how many dimes?: "))
                nickels = int(input("how many nickles?: "))
                pennies = int(input("how many pennies?: "))
                sum_total = round((quarter * quarters) + (dime * dimes) + (nickel * nickels) + (penny * pennies), 2)
                old_key = key
                if sum_total == cost:
                    print("Here you go ☕.")
                elif sum_total > cost:
                    change = sum_total - cost
                    print(f"Here's your coffee ☕, and here's your change: {change}$")
                else:
                    lacking = cost - sum_total
                    print(f"Sorry, looks like you're short {lacking}$")
        if coffee_type == "report":
            if old_key == "None":
                print(f"""We have {resources["water"]}ml water, {resources["milk"]}ml milk, and {resources
                ["coffee"]}g coffee in stock.""")
            else:
                print(f"""The {old_key.title()} contains {MENU[old_key]["ingredients"]["water"]}ml water, {MENU[old_key]
                ["ingredients"]["coffee"]}g coffee, and costs {MENU[old_key]["cost"]}$""")
            old_key = "None"


for name, ingredient in MENU.items():
    coffee_machine(name, ingredient["ingredients"]["water"], ingredient["ingredients"]["coffee"], ingredient["cost"])
