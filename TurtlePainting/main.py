from turtle import Turtle, Screen

# Creating tutle boi
squidward = Turtle()
squidward.shape('turtle')
squidward.color('green')

# Drawing a Triangle
def triangle():
    for _ in range(3):
        squidward.right(120)
        squidward.forward(100)

def square():
    for _ in range(4):
        squidward.right(90)
        squidward.forward(100)

def pentagon():
    for _ in range(6):
        squidward.right(60)
        squidward.forward(100)


triangle()
square()
pentagon()
def hexagon():
    pass
    # for _ in range





# Drawing a dotted line
# def draw_dotted(space, x):
#     for i in range(x):
#         squidward.penup()
#         for j in range(x):
#             squidward.dot()
#
#             squidward.forward(space)
#         squidward.backward(space*x)
#     squidward.penup()
#
#
#     squidward.hideturtle()
#
# draw_dotted(15, 20)
# Make a square
# for _ in range(4):
#     squidward.forward(100)
#     squidward.right(90)















# Creating screen module
screen = Screen()
screen.exitonclick()
