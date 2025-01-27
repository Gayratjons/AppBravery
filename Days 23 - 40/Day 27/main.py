from tkinter import *
window = Tk()
window.title("First GUI!")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = Label(text="Helloouuuu !", font=("Arial", 24))
my_label.config(text = "My text")
my_label.grid(column=0, row = 0)
#Button
# entry.pack()
def button_clicked():
    my_label["text"] = entry.get()
button = Button(text="Click me!", command=button_clicked)
button.grid(column=1, row = 1)
button1 = Button(text="Click me!", command=button_clicked)
button1.grid(column=0, row = 3)

entry = Entry(width=10)
entry.grid(column= 3, row = 4)




window.mainloop()