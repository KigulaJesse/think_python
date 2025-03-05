"""Book solutions to turtle exercise"""
from turtle import Screen, Turtle

def square_encap(t):
    "Encapsulation solution"
    for _ in range(4):
        t.fd(100)
        t.lt(90)


bob = Turtle()
square_encap(bob)


SCREEN = Screen()
SCREEN.mainloop()
