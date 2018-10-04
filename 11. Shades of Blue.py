#Name: Hashir Khan
#Date: September 27th, 2018
#This program creates a cone with different shades of blue
import turtle
turtle.colormode(255)
x = turtle.Turtle()
x.shape("turtle")
x.backward(100)
for i in range(0,255,10):
    x.forward(10)
    x.pensize(i)
    x.color(0,0,i)
