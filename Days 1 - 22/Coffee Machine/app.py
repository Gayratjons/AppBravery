coffee = str(input("What would you like to drink today (espresso, latte, cappucino):\n\t")).lower()
print("Please insert the amount of money in coins:")

recources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
coffee_menu = {
    "espresso": {
        "price": 1.50,
        "water": 50,  # in ml
        "coffee": 18  # in g
    },
    "latte": {
        "price": 2.50,
        "water": 200,  # in ml
        "coffee": 24,  # in g
        "milk": 150    # in ml
    },
    "cappuccino": {
        "price": 3.00,
        "water": 250,  # in ml
        "coffee": 24,  # in g
        "milk": 100    # in ml
    }
}
coins = {
    "Penny": 1,   # in cents
    "Nickel": 5,  # in cents
    "Dime": 10,   # in cents
    "Quarter": 25 # in cents
}
def coin_input():
    global coins
    summation = 0
    coin_input = coins
    for key in coin_input:
        coin_input[key] = input(f"Please input in {key}s:\n")
        print(coin_input[key])
        print(coins[key])
    # return summation
        
def recourses_reduce(coffee):
    global recources
    global coffee_menu
    recources["water"] -= coffee_menu[coffee]["water"]
    recources["coffee"] -= coffee_menu[coffee]["coffee"]
    recources["milk"] -= coffee_menu[coffee]["milk"]
    recourses["money"] += coffee_menu[coffee]["price"]

def coffee_making(coffee):
    global recources
    global coffee_menu
    if coffee == 'latte':
        recources["water"] -= coffee_menu[coffee]["water"]
        recources["coffee"] -= coffee_menu[coffee]["coffee"]
        recources["milk"] -= coffee_menu[coffee]["milk"]
        recources["money"] += coffee_menu[coffee]["price"]
    elif coffee == 'cappucino':
        recources["water"] -= coffee_menu[coffee]["water"]
        recources["coffee"] -= coffee_menu[coffee]["coffee"]
        recources["milk"] -= coffee_menu[coffee]["milk"]
        recources["money"] += coffee_menu[coffee]["price"]
    elif coffee == 'espresso':
        recources["water"] -= coffee_menu[coffee]["water"]
        recources["coffee"] -= coffee_menu[coffee]["coffee"]
        recources["money"] += coffee_menu[coffee]["price"]

# coffee_making(coffee)
# print(recources)
print(coin_input())




# if inpt == 'off':
#     state = False
# elif inpt == 'report':
#     for key in racources:
#         print(recources[key])
# elif inpt != 'latte' or inpt != 'cappucino' or inpt != 'espresso':
#     print("Wrong input!")  
