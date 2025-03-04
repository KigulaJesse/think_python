"""Right Justify Function"""

def right_justify(text:str):
    """This function right justifies a string by 70"""
    while True:
        text = " " + text
        if len(text) == 71:
            break
    print(text)
