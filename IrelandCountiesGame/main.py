import turtle
from functions import *

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title('Ireland Map')
screen.addshape('ireland.gif')
turtle.shape('ireland.gif')

# Reading the CSV
read = open('Ireland_Counties.csv', 'r')

# Counties
counties = []
for line in read:
    counties.append(line.lower().split(',')[1])

answer = screen.textinput(title='Ireland Map', prompt='Name a county!')

while answer.lower() != 'done':
    if answer in counties:
        print(answer)
    else:
        print('incorrect')
    answer = screen.textinput(title='Ireland Map', prompt='Name a county!')

# Getting co-ordinates on click
# turtle.onscreenclick(get_position_on_click)
# turtle.mainloop()


# screen.exitonclick()
