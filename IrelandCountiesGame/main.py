import turtle
from functions import *

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title('Ireland Map')

screen.addshape('ireland.gif')

turtle.shape('ireland.gif')

# Getting co-ordinates on click
turtle.onscreenclick(get_position_on_click)
turtle.mainloop()


# screen.exitonclick()
