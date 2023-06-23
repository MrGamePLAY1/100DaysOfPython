import tkinter as tk

#     __  ____ __               __       __ __
#    /  |/  (_) /__  _____      \ \     / //_/____ ___
#   / /|_/ / / / _ \/ ___/  _____\ \   / ,<  / __ `__ \
#  / /  / / / /  __(__  )  /_____/ /  / /| |/ / / / / /
# /_/  /_/_/_/\___/____/        /_/  /_/ |_/_/ /_/ /_/
#


window = tk.Tk()
window.title("Converter")
window.minsize(width=50, height=70)

# input box
user_input = tk.Entry()


# Functions
def calculate():
    try:
        floater_user_input = float(user_input.get())
        output = floater_user_input * 1.609
        value.config(text=output)
    except ValueError:
        value.config(text="Invalid input")


# Labels
miles_text = tk.Label(text='Miles', font=('Arial', 12, 'bold'))
miles_text.place()

is_equal = tk.Label(text='is equal to ', font=('Arial', 8, 'bold'))
is_equal.place()

value = tk.Label(text=0)
value.place()

km = tk.Label(text='Km', font=('Arial', 8, 'bold'))
km.place()

# Buttons
button = tk.Button(text='Calculate', command=calculate)

# Layouts
user_input.grid(row=0, column=2, padx=15)
miles_text.grid(row=0, column=3)
is_equal.grid(row=1, column=0, )
value.grid(row=1, column=2)
km.grid(row=1, column=3)
button.grid(row=2, column=2)

window.mainloop()
# Do not put code below here
