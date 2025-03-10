"""Pratise for recursion and conditionals"""

def countdown(n):
    "Simple Countdown"
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

def print_n(s, n):
    "prints string n times"
    if n <=0:
        return
    print(s)
    print_n(s, n-1)

# print_n("Hello",2)

def do_n(func,string,string_n,n):
    "Calls function n times"
    if n <=0:
        return
    func(string,string_n)
    do_n(func,string,string_n,n-1)

do_n(print_n,"Hello",3,5)
