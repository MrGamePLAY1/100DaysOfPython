from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flash')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=card_front_image)

# Text
canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))

canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
correct_button = Button(image=check_image)
correct_button.grid(row=1, column=1)



window.mainloop()