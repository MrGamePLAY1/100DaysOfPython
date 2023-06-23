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
fg = GREEN
check_mark = '✔'

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Timer')
window.minsize(height=500, width=500)
window.config(padx=100, pady=50, bg=YELLOW)


# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)
canvas.create_text(100, 132, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.place()
canvas.grid(row=2, column=1)

# Buttons
start = Button(text='Start', font=('Arial', 10, 'bold'))
start.place()
start.grid(row=3, column=0)

reset = Button(text='Reset', font=('Arial', 10, 'bold'))
reset.place()
reset.grid(row=3, column=2)

# Label
timer_text = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'))
timer_text.place()
timer_text.grid(row=1, column=1)

check_text = Label(text='✔', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_text.place()
check_text.grid(row=4, column=1)



window.mainloop()


# ✔