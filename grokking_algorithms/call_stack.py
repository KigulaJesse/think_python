"The call stack"

def greet(name):
    "greet"
    print("Hello, " + name + "!")
    greet2(name)

def greet2(name):
    "greet2"
    print("How are you, " + name + "?")

    def bye():
        "inner bye"
        print("ok bye!")