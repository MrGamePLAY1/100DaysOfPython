import tkinter as tk
from tkinter import *

import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
fg = GREEN
check_mark = '✔'
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text_inital, text='00:00')
    timer_text.config(text='Timer', fg=GREEN)
    check_text.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    # work_sec = 5
    work_sec = WORK_MIN * 60  # 25 minutes
    # print(work_sec)
    short_break_sec = SHORT_BREAK_MIN * 60  # 5 minutes
    # short_break_sec = 4
    # print(short_break_sec)
    long_break_sec = LONG_BREAK_MIN * 60  # 20 minutes
    # print(long_break_sec)

    if reps % 1 == 0:
        reps += 1
        count_down(work_sec)
        # @TODO: MAKE THIS WORK WITH MULTIPLE TICKS IN A ROW
        timer_text.config(text='WORK', fg=GREEN)
        if reps % 2 == 0:
            count_down(short_break_sec)
            timer_text.config(text='BREAK', fg=PINK)
            if reps % 8 == 0:
                count_down(long_break_sec)
                timer_text.config(text='LONG BREAK', fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minute = count // 60
    second = count % 60
    if second < 10:
        second = f'0{second}'
    if second == 0:
        second = '00'
    canvas.itemconfig(timer_text_inital, text=f'{minute}:{second}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''

        for i in range(math.floor(reps / 2)):
            mark += check_mark
        check_text.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Timer')
window.minsize(height=500, width=500)
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)
timer_text_inital = canvas.create_text(100, 132, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.place()
canvas.grid(row=2, column=1)

# Buttons
start = Button(text='Start', command=start_timer, font=('Arial', 10, 'bold'))
start.place()
start.grid(row=3, column=0)

reset = Button(text='Reset', command=reset_timer, font=('Arial', 10, 'bold'))
reset.place()
reset.grid(row=3, column=2)

# Label
timer_text = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'))
timer_text.place()
timer_text.grid(row=1, column=1)

timer_text.config(text='WORK', fg=GREEN)
check_text = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_text.place()
check_text.grid(row=4, column=1)

window.mainloop()
# Keep code above here

# ✔
