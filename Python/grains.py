def square(number):
    """
    Calculate the value of grains of wheat based on the square
    
    Parameter number: int - the given square were the amount of grains must be calculated.
    """
    
    if (number < 1 or number > 64):
        raise ValueError("square must be between 1 and 64")
    result = 2**(number - 1)
    return result


def total():
    """
    Calculate the total number of grains on the chessboard
    
    Calculate the value of grains of wheat of each square and add them 
    """
    i = 0
    result = 0
    while i < 64:
      result = result + 2**(i)
      i += 1
    return result
