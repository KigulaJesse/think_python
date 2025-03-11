"""Checks Femats theorem"""

def check_femat(a,b,c,n):
    "Checks Femat"
    to_check = (a**n) + (b**n)
    c_powered = c**n
    if n > 2 and c_powered == to_check:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")

while True:
    print("Let's confirm Femat's Theory\n")
    a_input = int(input("Enter a:"))
    b_input = int(input("Enter b:"))
    c_input = int(input("Enter c:"))
    n_input = int(input("Enter n:"))

    check_femat(a_input,b_input,c_input,n_input)
    print("")
    to_exit = input("Check Again! Y for yes else N for no: ")
    if to_exit == "N":
        break
