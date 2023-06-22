import tkinter

window = tkinter.Tk()
window.title("Custom Title")
window.minsize(width=600, height=600)

# Components

# Labels
label = tkinter.Label(text='I am a label', font=("Arial", 14, "bold"))
label.pack()

# Button
button = tkinter.Button(text='Button')
button2 = tkinter.Button(text='New Button')
button.place()
button2.place()

# Entry
user_input = tkinter.Entry()
user_input.place()

# Layout
label.grid(row=0, column=0)
button.grid(row=1, column=2)
button2.grid(row=0, column=3)
user_input.grid(row=3, column=4)




window.mainloop()
# Do not put code below here