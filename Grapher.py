"""
Rahul Shah
Takes a text or LATEX file and graphs a bunch of points
Connected by lines
Using turtle
"""

import turtle

turtle.setposition(-100,100)

y1 = 0

with open("Points.txt") as file:
    for word in file:
        for ch in file:
            if(float(word)<1):
                   y2 = (word * 100)
                   turtle.left(degrees(atan((y2-y1)/10)))
                   turtle.forward(tan((y2-y1)/10))
                   y1 = y2


