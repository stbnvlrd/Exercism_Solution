import math

def score(x, y):
    dist = math.sqrt((x**2)+(y**2))
    if dist > 10:
        points = 0
    elif dist > 5:
        points = 1
    elif dist > 1:
        points = 5
    elif dist <= 1:
        points = 10
    return points
