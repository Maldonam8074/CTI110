# CTI-110
# M5LAB
# Manuel Maldonado
# 10/16/2017

import turtle
import random
win = turtle.Screen()
mo = turtle.Turtle()
win.bgcolor("grey")

colours = ["cyan", "purple", "white", "darkblue"]

# Options
mo.pensize(4)
mo.shape("turtle")

# Shape

# Move turtle to center of page
mo.up()
mo.left(90)
mo.forward(100)
mo.left(90)
mo.forward(100)
mo.right(90)
mo.right(90)
mo.down()

# loop for turtle
for i in range (12):
    mo.forward(250)
    mo.right(60)
    mo.forward(200)
    mo.right(60)
    mo.forward(150)
    mo.right(60)
    mo.right(30)
    mo.color(random.choice(colours))

# close loop
win.mainloop()  
