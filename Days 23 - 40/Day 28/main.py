from itertools import count
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =  25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def clear_screen():
    global checkpoint
    global timer_label
    checkpoint.config(text="")
    timer_label.config(text = "Timer", font = (FONT_NAME, 40, "bold"),fg = GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
def reset_timer():
    window.after_cancel(timer)
    clear_screen()
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Rest!", fg="#16C47F")
    if reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break!", fg="#A9C46C")
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work!", fg="red")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✔"
            checkpoint.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Scheme")
window.config(padx=50, pady=50, bg=YELLOW)
text = "✔"

timer_label = Label(text = "Timer", font = (FONT_NAME, 40, "bold"),fg = GREEN, bg=YELLOW)
timer_label.grid(column = 1, row = 0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_png)
timer_text = canvas.create_text(100,112, text="00:00", fill="white", font = (FONT_NAME, 30, "bold"))
canvas.grid(column = 1, row = 1)


start_button = Button(text="Start", width=7, command=start_timer)
start_button.grid(column=0, row=3)
reset_button = Button(text="Reset", width=7, command=reset_timer)
reset_button.grid(column=2, row=3)

checkpoint = Label(bg=YELLOW, fg=GREEN)
checkpoint.grid(column=1, row=4)
window.mainloop()