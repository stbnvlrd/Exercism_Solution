def answer(question):
    equation = question[8:-1]
    equation = equation.replace(" by ", " ")
    split_equation = equation.split()
    print(split_equation)
    if len(split_equation) == 1:
        return(int(split_equation[0]))
    if len(split_equation) == 0:
        raise ValueError("syntax error")
    elif len(split_equation) == 5:
        if split_equation[1] == "plus":
            first_op = (int(split_equation[0]) + int(split_equation[2]))
        elif split_equation[1] == "minus":
            first_op = (int(split_equation[0]) - int(split_equation[2]))
        elif split_equation[1] == "multiplied":
            first_op = (int(split_equation[0]) * int(split_equation[2]))
        elif split_equation[1] == "divided":
            first_op = (int(split_equation[0]) / int(split_equation[2]))
        else:
            raise ValueError("unknown operation")
        if split_equation[3] == "plus":
            return (first_op + int(split_equation[4]))
        elif split_equation[3] == "minus":
            return (first_op - int(split_equation[4]))
        elif split_equation[3] == "multiplied":
            return (first_op * int(split_equation[4]))
        elif split_equation[3] == "divided":
            return (first_op / int(split_equation[4]))
        else:
            raise ValueError("unknown operation")
    elif len(split_equation) == 2:
        raise ValueError("syntax error")
    elif len(split_equation) == 3:
        if split_equation[1] == "plus":
            return(int(split_equation[0]) + int(split_equation[2]))
        elif split_equation[1] == "minus":
            return(int(split_equation[0]) - int(split_equation[2]))
        elif split_equation[1] == "multiplied":
            return(int(split_equation[0]) * int(split_equation[2]))
        elif split_equation[1] == "divided":
            return(int(split_equation[0]) / int(split_equation[2]))
        else:
            raise ValueError("unknown operation")
    else:
        raise ValueError("unknown operation")
