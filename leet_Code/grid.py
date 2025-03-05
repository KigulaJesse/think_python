"""Function to draw a grid"""

def draw_columns(columns, starter, separator):
    """draws columns"""
    for column in range(columns):
        print(starter,separator*4,end=" ")
        if column + 1 == columns:
            print(starter)

def draw_rows(columns):
    """draws rows"""
    x = 0
    while True:
        draw_columns(columns, "|"," ")
        x = x + 1
        if x == 4:
            break

def draw_grid(columns, rows):
    "prints grid"
    for row in range(rows):
        draw_columns(columns, "+","-")
        draw_rows(columns)
    draw_columns(columns, "+","-")

draw_grid(2,2)
