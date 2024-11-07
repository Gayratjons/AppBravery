import replit from clear
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
    if player_sum > dealer_sum:
        return player_sum
    else:
        return dealer_sum

def play_game():
    for i in range(2):
        player_cards[i] = deal_card()
        dealer_cards[i] = deal_card()
    print("Your cards are: ", player_cards[:2])
    print("Dealer card is: ", dealer_cards[0])
    choice = input("Do you want another card or you want to end the game and see who wins ? (print 'y' or 'n')")
    if choice == 'y':
        player_cards += deal_card()
    else:
        print(choose_the_winner(player_cards, dealer_cards))

state = True
    while state:
        choice = str(input("Do you want to play Black-Jack game? (type 'y' or 'n')"))
        if choice == 'y':
            clear()
            print_logo()
        elif choice == 'n':
            state = False
        else:
            print("Wrong Input!")
