resistors_color = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
    }

def value(colors):
    value = 0
    for x in range(2):
        value = value + (resistors_color[colors[x]]) * (10**(1 - x))
    return value
