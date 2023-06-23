import tkinter as tk
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Timer')
window.minsize(height=500, width=500)
window.config(padx=100, pady=50, bg=YELLOW)


# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW)
image = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=image)
canvas.create_text(102, 132, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.pack()



window.mainloop()