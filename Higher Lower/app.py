import random
import os
from Obj import top_50_instagram_accounts as instagram_top_followed
source = list(instagram_top_followed.keys())
def randomise():
    global source
    rand_key = random.choice(source)
    return rand_key
def check_higher(key1, key2, action):
    arr = []
    global instagram_top_followed
    value_1 = instagram_top_followed[key1]
    value_2 = instagram_top_followed[key2]
    if action == 'h':
        if value_1 > value_2:
            return key1
        else:
            return 'Lose'
    elif action == 'l':
        if value_2 > value_1:
            return key2
        else:
            return 'Lose'
def switch_order(key):
    global source
    source.remove(key)

print("Welcome to Higher-Lower game")
state = True
key1 = randomise()
while state:
    key2 = randomise()
    print(len(source))
    print(f"Hint: {instagram_top_followed[key1]} and {instagram_top_followed[key2]}")
    print(f"Does {key1} have more subscribers or {key2}")
    ask = str(input("Print 'h' to pick higher or 'l' to pick lower options:\n\t")).lower()
    checkout = check_higher(key1, key2, ask)
    if ask != 'h' and ask != 'l':
        print("Wrong input!")
    else:
        checkout = check_higher(key1, key2, ask)
    if checkout != 'Lose':
        key1 = checkout
        switch_order(key2)
        os.system('clear')
    elif len(source) == 0:
        print("Sorry! We are run out of ceebities :)")
        state = False
    else:
        print("Oh! That was a wrong choice :(")
        state = False