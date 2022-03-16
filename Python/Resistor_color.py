def color_code(color):
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
    return resistors_color[color]

def colors():
    expected = ["black", "brown", "red", "orange", "yellow", 
                "green", "blue", "violet", "grey", "white"
        ]
    return expected
