"""Pratise for recursion and conditionals"""

def countdown(n):
    "Simple Countdown"
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

countdown(600)
