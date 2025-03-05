"Testing do twice"

def print_spam():
    """Prints the word spam"""
    print("spam")

def print_my_word(my_word):
    """Prints the word I have passed to it"""
    print(my_word)

def print_twice(bruce):
    "prints a string twice"
    print(bruce)
    print(bruce)

def do_twice(func, value):
    """Calls a function twice"""
    func(value)
    func(value)

def do_four(func, value):
    """Calls a function four times"""
    do_twice(func, value)
    do_twice(func, value)

# do_twice(print_twice, "spam")
do_four(print_my_word, "spam")
