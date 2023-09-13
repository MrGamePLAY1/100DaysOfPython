from tkinter import *
import pandas as pd
import random

current_word = {}
data = pd.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient='records')


def random_word():
    global current_word
    french = data['French'].to_list()
    current_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(card_word, text=current_word['French'])


def french_to_english():
    canvas.create_image(400, 263, image=card_back_image)
    canvas.itemconfig(card_title, text='English')
    canvas.itemconfig(card_word, text=current_word['English'])
    canvas.itemconfig(background, image=card_back_image)




# french_to_english()

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flash')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)

# Front and background images
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')

background = canvas.create_image(400, 263, image=card_front_image)
window.after(3000, func=french_to_english)

# Text
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 30, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))

canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image, highlightthickness=0, command=random_word)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
correct_button = Button(image=check_image, highlightthickness=0, command=random_word)
correct_button.grid(row=1, column=1)


# Start displaying the new French word
random_word()
window.mainloop()