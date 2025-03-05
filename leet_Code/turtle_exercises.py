"""Turtle Exercises from book"""
from turtle import Screen, Turtle
import math

def square(t,length):
    """Function draws Square"""
    for _ in range(4):
        t.fd(length)
        t.rt(90)

def polygon(t,n,length,final_angle=360):
    "Function that draws a polygon"
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        if i == final_angle:
            break

def book_circle(t,r):
    """Book circle"""
    circumference = 2* math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t,n,length)

def draw_circle(t,r):
    """Function that draws a circle"""
    polygon(t,360,r)

def arc(t,r,angle):
    """Draws a fraction of a circle"""
    polygon(t,360,r,angle)



bob = Turtle()
book_circle(bob,100)
#Testing various lengths
# square(bob,200)
# square(bob,400)
# polygon(bob,6,50)
# polygon(bob,6,100)
# polygon(bob,6,200)
# draw_circle(bob,1)
#arc(bob,1,270)

SCREEN = Screen()
SCREEN.mainloop()
