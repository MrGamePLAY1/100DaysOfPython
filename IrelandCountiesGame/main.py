import turtle
from functions import *
import pandas as pd

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title('Ireland Map')
screen.addshape('ireland.gif')
turtle.shape('ireland.gif')

# Reading the CSV
read = pd.read_csv('ireland.csv')
all_counties = read.County.to_list()
guessed_counties = []
print(guessed_counties)

answer = screen.textinput(title='Ireland Map', prompt='Name a county!')
score = 0

while answer != 'done':
    if answer in all_counties:
        if answer in guessed_counties:
            score -= 1
            print('You already guessed that!')
            print(guessed_counties)
        guessed_counties.append(answer)
        score += 1
        screen.title('Ireland Map - Score: ' + str(score) + '/33')
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        county_selected = read[read.County == answer]
        t.goto(int(county_selected.x), int(county_selected.y))
        t.write(answer, font=('Arial', 10, 'normal'))
        if score == 33:
            print('You win!')
            break

    else:
        print('incorrect')
    answer = screen.textinput(title='Ireland Map', prompt='Name a county!')

# Getting co-ordinates on click
# turtle.onscreenclick(get_position_on_click)
# turtle.mainloop()


# screen.exitonclick()
