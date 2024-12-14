import random
import os
choice = input("Do you want to play Guess THe Number game in 'hard' or 'easy' level?\n")
if choice == 'easy':
    lifes = 10
    os.system('cls')
elif choice == 'hard':
    lifes = 5
    os.system('cls')
else:
    print("Wrong Input")
rand_num = random.randint(1,100)
state = True
def calc(guess):
    os.system('cls')
    global lifes
    global state
    print(f"You have {lifes} lifes left")
    if lifes > 0:
        if guess > rand_num:
            print("Too high!\n")
            lifes -= 1
        elif guess == rand_num:
            print("You found the number. Great! :)")
            state = False
        else:
            print("Too low!\n")
            lifes -= 1
    else:
        print(f"Sorry you lost :(\nThe number was: {rand_num}")
        state = False
while state:
    guess = int(input("Please guess a number from 1-100\n"))
    calc(guess)
