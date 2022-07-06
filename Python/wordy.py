def answer(question):
    equation = question[8:-1]
    split_equation = equation.split()
    if split_equation[1] == "plus":
        return(int(split_equation[0]) + int(split_equation[2]))
    elif split_equation[1] == "minus":
        return(int(split_equation[0]) - int(split_equation[2]))
    elif split_equation[1] == "multiplied":
        return(int(split_equation[0]) * int(split_equation[3]))
    elif split_equation[1] == "divided":
        return(int(split_equation[0]) / int(split_equation[3]))

