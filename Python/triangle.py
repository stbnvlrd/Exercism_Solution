def not_degenerate(sides):
    """
    Determine if a triangle is degenerate 
    
    Parameter sides: list of int - with the given sides, we can determine if a triangle is degenerate .
    """
    
    sides.sort()
    a,b,c = sides
    return ((a + b) > (c))

def size_not_0(sides):
    a,b,c = sides
    return a != 0 or b != 0 or c != 0

def equilateral(sides):
    """
    Determine if a triangle is equilateral
    
    Parameter sides: list of int - with the given sides, we can determine if a triangle is equilateral.
    """
    a,b,c = sides
    return size_not_0(sides) and a == b == c



def isosceles(sides):
    """
    Determine if a triangle is isosceles
    
    Parameter sides: list of int - with the given sides, we can determine if a triangle is isosceles.
    """
    
    
    a,b,c = sides
    
    return not_degenerate(sides) and size_not_0(sides) and (a == b or b == c or a == c)
        

def scalene(sides):
    """
    Determine if a triangle is scalene
    
    Parameter sides: list of int - with the given sides, we can determine if a triangle is scalene.
    """

    
    a,b,c = sides
    
    return not_degenerate(sides) and size_not_0(sides) and a != b != c != a
    
