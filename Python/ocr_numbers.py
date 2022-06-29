def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    else:
        for row in input_grid:
            if len(row) % 3 != 0:
                raise ValueError("Number of input columns is not a multiple of three")
        
        
            number = input_grid
            if number == [" _ ", "| |", "|_|", "   "]:
                decimal_number = "0"
            elif number == ["   ", "  |", "  |", "   "]:
                decimal_number = "1"
            elif number == [" _ ", " _|", "|_ ", "   "]:
                decimal_number = "2"
            elif number == [" _ ", " _|", " _|", "   "]:
                decimal_number = "3"
            elif number == ["   ", "|_|", "  |", "   "]:
                decimal_number = "4"
            elif number == [" _ ", "|_ ", " _|", "   "]:
                decimal_number = "5"
            elif number == [" _ ", "|_ ", "|_|", "   "]:
                decimal_number = "6"
            elif number == [" _ ", "  |", "  |", "   "]:
                decimal_number = "7"
            elif number == [" _ ", "|_|", "|_|", "   "]:
                decimal_number = "8"
            elif number == [" _ ", "|_|", " _|", "   "]:
                decimal_number = "9"
            else:
                decimal_number = "?"
    return decimal_number
    
print(convert(["    _  _     _  _  _  _  _  _ ", "  | _| _||_||_ |_   ||_||_|| |", "  ||_  _|  | _||_|  ||_| _||_|", "                              ",]))