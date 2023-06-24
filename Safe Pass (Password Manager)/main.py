from tkinter import *

# ------------------- Password Generator ------------------- #
def generate_password():
    pass

# ------------------- Saving Password  --------------------- #


# ------------------- UI ----------------------------------- #
window = Tk()
window.title("Safe Pass")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
image = PhotoImage(file='icon.png')
canvas.create_image(100, 100, anchor=CENTER,  image=image)
canvas.place()
canvas.grid(row=0, column=1)


# Labels
website = Label(text="Website:")
email = Label(text="Email/Username:")
password = Label(text="Password:")

website.grid(row=1, column=0)
email.grid(row=2, column=0)
password.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2)


window.mainloop()
# Do not put code below here