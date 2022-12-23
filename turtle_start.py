# https://docs.python.org/3/library/turtle.html

import turtle

t = turtle.Turtle()

# turtle.setup(1280, 960)
# turtle.screensize(400, 300)
t.speed("fastest")
t.shape("turtle")
t.turtlesize(2)
t.color("green")
t.pencolor("blue")
t.screen.bgcolor("aqua")

# for i in range(8):
#     for i in range(4):
#         t.forward(200)
#         t.left(90)
#     t.left(45)

# for i in range(6):
#     for i in range(3):
#         t.forward(200)
#         t.left(120)
#     t.left(60)

for i in range(12):
    for i in range(6):
        t.forward(200)
        t.left(60)
    t.left(30)

turtle.done()
