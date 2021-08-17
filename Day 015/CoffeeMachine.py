MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coin. ")
    total=int(input("How many ₹10 coin? :"))*10
    total+=int(input("How many ₹5 coin? :"))*5
    total+=int(input("How many ₹2 coin? :"))*2
    total+=int(input("How many ₹1 coin? :"))*1
    return total

def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = money_recieved - drink_cost
        print(f"Here is your ₹{change} in change.")
        global profit
        profit+=drink_cost
        return True

    else:
        print(f"Sorry, It's ₹{money_recieved}.That's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name.capitalize()} ☕.Enjoy!")

is_on = True
while is_on :
    choice = input("\nWhat would you like? (espresso (₹15) / latte (₹25) / cappuccino (₹30) ): ")
    if choice == "off":
        is_on =False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ₹{profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])