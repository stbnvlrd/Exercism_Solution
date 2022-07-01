def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    else:
        for row in input_grid:
            if len(row) % 3 != 0:
                raise ValueError("Number of input columns is not a multiple of three")
        
        column_division = (len(input_grid[0])//3)
        # letter_list_model = ["","","",""]
        
        if len(input_grid) > 4:
            input_lines = ['','','','']
            for row in range(len(input_grid)):
                input_lines[row%4] = input_lines[row%4] + input_grid[row]
        else:
            input_lines = input_grid
        numbers = [[] for i in range(column_division)]
        print(numbers)
        for row in range(len(input_lines)):
            for column in range(len(input_lines[row])):
                # print(str(row) + ", " + str(column//3))
                # print(input_lines[row][column])
                if column % 3 == 0:
                    numbers[column//3].append(input_lines[row][column])
                else:
                    numbers[column//3][row] = numbers[column//3][row] + input_lines[row][column]
            # print(numbers)
        # print(numbers)
        result = ""
        for number in numbers:
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
            result = result + decimal_number
    return result

print(convert(["    _  _     _  _  _  _  _  _ ", "  | _| _||_||_ |_   ||_||_|| |", "  ||_  _|  | _||_|  ||_| _||_|", "                              ",]))