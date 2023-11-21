import turtle
import math

'''
x = 250
'''
a = 15

pen = turtle.Turtle()
pen.color("red", "blue")
pen.speed(10)

pen.begin_fill()

for contador in range(12):
    pen.forward(300)
    pen.left(a)
    pen.forward(-300)
    pen.left(a)
pen.end_fill()

turtle.done()
