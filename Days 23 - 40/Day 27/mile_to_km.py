from tkinter import *
window = Tk()
window.title("Mile to Kilometre")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

entry = Entry(width=7)
entry.grid(column=2, row=0)

miles = Label(text = "Miles")
miles.grid(column=3, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=1, row=1)

mile_km = Label(text="0")
mile_km.grid(column=2, row=1)

km = Label(text="Km")
km.grid(column=3, row=1)

def action():
    mile_km.config(text=f"{(int(entry.get()) * 1.60934)}")

#calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=2, row=2)



window.mainloop()
