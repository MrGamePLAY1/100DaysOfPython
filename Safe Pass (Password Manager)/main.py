from tkinter import *

# ------------------- Password Generator ------------------- #
def generate_password():
    pass

# ------------------- Saving Password  --------------------- #
# Take all the entrys put in and save them in a file
def save_password():
    pass


# ------------------- UI ----------------------------------- #
window = Tk()
window.title("Safe Pass")
window.minsize(width=450, height=400)
window.config(padx=50, pady=50)

# Centering the window on the screen
window.eval('tk::PlaceWindow . center')

canvas = Canvas(window, width=200, height=200)
image = PhotoImage(file='icon.png')
canvas.create_image(100, 100, anchor=CENTER, image=image)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
website = Label(window, text="Website:")
email = Label(window, text="Email:")
password = Label(window, text="Password:")

website.grid(row=1, column=0)
email.grid(row=2, column=0)
password.grid(row=3, column=0)

# Entries
website_entry = Entry(window, width=43)
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()

email_entry = Entry(window, width=43)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)

password_entry = Entry(window, width=22)
password_entry.grid(row=3, column=1, pady=5)

# Buttons
generate_pass = Button(window, text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2, pady=5, padx=12, sticky=W)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
