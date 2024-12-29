import os
import random


def print_logo():
    blackjack_logo = [
        "  ____  _            _        _            _        _      ",
        " | __ )| | __ _  ___| | __   | | __ _  ___| | __   | |   __ _ ",
        " |  _ \\| |/ _` |/ __| |/ /   | |/ _` |/ __| |/ /   | |  / _` |",
        " | |_) | | (_| | (__|   <    | | (_| | (__|   <    | | | (_| |",
        " |____/|_|\\__,_|\\___|_|\\_\\   |_|\\__,_|\\___|_|\\_\\   |_|  \\__,_|",
        "                                                              ",
        "                     BLACKJACK                                ",
        "                                                              ",
        "            .------.           .------.                      ",
        "            |A .   |           |K  .  |                      ",
        "            | / \\  |           | / \\  |                      ",
        "            |(_,_) |           |(_,_) |                      ",
        "            |  I  A|           |  I  K|                      ",
        "            `------'           `------'                      ",
    ]
    for line in blackjack_logo:
        print(line)
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10]
    return random.choice(cards)
def choose_the_winner(*a):
    player_sum = 0
    dealer_sum = 0
    for i in a[0]:
        player_sum += i
    for i in a[1]:
        dealer_sum += i
    if player_sum > dealer_sum and player_sum <= 21:
        return f"Player wins with {player_sum} points"
    elif player_sum == dealer_sum and (player_sum <= 21 and dealer_sum <= 21):
        return f"Tie. Both having {player_sum} points"
    elif player_sum < dealer_sum and dealer_sum <= 21:
        return f"Dealer wins with {dealer_sum} points"
    else:
        return f"Game over, player: {player_sum}; dealer: {dealer_sum}"
def start_game():
    player_cards = []
    dealer_cards = []
    for i in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())
    print("Your cards are: ", player_cards[:2])
    print("Dealer's card is: ", dealer_cards[0])
    choice = input("Do you want a card or end the game ? (type 'y' or 'n'\n")
    if choice == 'y':
        continue_game(player_cards, dealer_cards)
    elif choice == 'n':
        print(choose_the_winner(player_cards, dealer_cards))

def continue_game(player_cards, dealer_cards):
    choice = 'y'
    while sum(player_cards) <= 21 and choice == 'y':
        player_cards.append(deal_card())
        print("Your cards are:", player_cards)
        print("Dealer's first card is:", dealer_cards[0])
        if sum(player_cards) > 21:
            print("You have exceeded 21!")
            break
        choice = input("Do you want a card or end the game ? (type 'y' or 'n'\n")
    else:
        print("Ending game...")
    print(choose_the_winner(player_cards, dealer_cards))
print_logo()
choice = str(input("Do you want to play Black-Jack game? (type 'y' or 'n')\n"))
if choice == 'y':
    os.system('clear')
    start_game()
elif choice == 'n':
    print("Ok let's see you next time :)")
else:
    print("Wrong Input!")