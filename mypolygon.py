"""Testing graphics"""
from turtle import Screen, Turtle

bob = Turtle()
for i in range(4):
    bob.fd(100)
    bob.lt(90)

SCREEN = Screen()
SCREEN.mainloop()
