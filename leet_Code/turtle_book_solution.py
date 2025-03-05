"""Book solutions to turtle exercise"""
from turtle import Screen, Turtle
import math

def square_encap(t):
    "Encapsulation solution"
    for _ in range(4):
        t.fd(100)
        t.lt(90)

def square_gen(t,length):
    "generalization solution because of length"
    for _ in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t,n,length):
    "Also generalization but draws any polygon"
    angle = 360/n
    for _ in range(n):
        t.fd(length)
        t.lt(angle)

def poly_line(t,n,length,angle):
    "Draws a line"
    for _ in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t,r,angle):
    """Function draws a arc"""
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    poly_line(t,n,step_length, step_angle)

def circle(t,r):
    "draws a circle of radius r"
    arc(t,r,360)


bob = Turtle()
# square_encap(bob)
# square_gen(bob,100)
# polygon(bob,3,100)
# circle(bob,100)
arc(bob,100,270)


SCREEN = Screen()
SCREEN.mainloop()
