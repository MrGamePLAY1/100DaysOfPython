import random
from tkinter import *
from random import randint
from tkinter import messagebox
import json


# ------------------- Password Generator ------------------- #
def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+1234567890"
    final_password = random.sample(characters, randint(12, 16))

    password_entry.insert(0, "".join(final_password))
    read_for_passwords()


# ------------------- Saving Password  --------------------- #
# Take all the entrys put in and save them in a file
def save_password():
    not_saved = True

    while not_saved:
        if website_entry.get() == "" or email_entry.get() == "" or password_entry.get() == "":
            validations()
            break
        else:
            # Read current passwords in file
            with open('passwords.json', 'w') as data_file:

                # Getting elements
                website_contents = website_entry.get()
                email_contents = email_entry.get()
                password_contents = password_entry.get()

                new_data = {
                    website_contents: {
                        'email': email_contents,
                        'password': password_contents,
                    }
                }

                json.dump(new_data, data_file, indent=4)

                success_label = Label(window, text="Success!", fg="green")
                success_label.grid(row=4, column=0)
                window.after(2000, remove_label, success_label)
                not_saved = False

    # Clearing all the feeds
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)

    website_entry.focus()


def validations():
    if website_entry.get() == "" or email_entry.get() == "" or password_entry.get() == "":
        messagebox.showwarning("Warning", "You have empty fields!")


def remove_label(success_label):
    success_label.destroy()


def read_for_passwords():
    with open('passwords.json', 'r') as data_file:
        data_file = json.load(data_file)
        print(data_file)


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

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()