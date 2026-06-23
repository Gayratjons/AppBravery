from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/kor_eng.csv")
else:
    pass
finally:
    data_dict = data.to_dict(orient="records")


current_card = {}
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="Korean", fill="black")
    canvas.itemconfig(card_word, text=current_card["Korean"], fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()



window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Umar's flashy card game")
flip_timer = window.after(3000, flip_card)
# -------------------------------------- UI SETUP -----------------------------------------------------
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 230, font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_button_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_button_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_button_imgage = PhotoImage(file="images/right.png")
known_button = Button(image=check_button_imgage, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)
next_card()
window.mainloop()