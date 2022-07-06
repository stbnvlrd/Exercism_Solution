def answer(question):
    equation = question[8:-1]
    split_equation = equation.split()
    if len(split_equation) == 1:
        return(int(split_equation[0]))
    if len(split_equation) == 0:
        raise ValueError("syntax error")
    elif len(split_equation) > 4 and split_equation[0].isdecimal():
        return ("multiple")
    elif len(split_equation) == 2:
        raise ValueError("syntax error")
    elif len(split_equation) > 2 and len(split_equation) < 5:
        if split_equation[1] == "plus":
            return(int(split_equation[0]) + int(split_equation[2]))
        elif split_equation[1] == "minus":
            return(int(split_equation[0]) - int(split_equation[2]))
        elif split_equation[1] == "multiplied":
            return(int(split_equation[0]) * int(split_equation[3]))
        elif split_equation[1] == "divided":
            return(int(split_equation[0]) / int(split_equation[3]))
        else:
            raise ValueError("unknown operation")
    else:
        raise ValueError("unknown operation")
    pass
