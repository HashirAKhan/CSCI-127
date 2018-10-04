#Name:Hashir Khan
#Date: September 27, 2018
#This project creates a block spiral
import turtle
x = turtle.Turtle()

for i in range(251):
    if (i % 10 == 0 and i != 0):
        x.forward(i)
        x.left(90)
