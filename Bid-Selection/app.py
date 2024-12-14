import os
bid_dict = {}
state = True
yes_no = ""

def bid_selection():
    temp_key = ""
    first_bid = bid_dict[list(bid_dict.keys())[0]]
    for key in bid_dict:
        if bid_dict[key] > first_bid:
            first_bid = bid_dict[key]
            temp_key = key
    print(f"{temp_key} gets the item for {first_bid}")
while state:
    os.system('cls')
    name = str(input("What is your name ?\n"))
    bid = int(input("How much is your bid ? $"))
    yes_no = str(input("Is there anyone else with bill (type yes or no)?\n"))
    bid_dict[name] = bid  
    if yes_no == "no":
        bid_selection()
        state = False