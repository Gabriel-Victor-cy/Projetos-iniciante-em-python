import turtle
import math

angle = 5
distance = 250
pen = turtle.Turtle()
dimension = abs(round(((360 / angle) / 2)))
print(dimension)
pen.speed(10000)

for contador in range(dimension):
    pen.forward(distance)
    pen.right(angle)
    pen.forward(-distance)
    pen.right(angle)

turtle.done()
