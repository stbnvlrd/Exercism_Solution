def is_paired(input_string):
    result = False
    new_string = ""
    for index in range(len(input_string)):
        if input_string[index] != '(' and input_string[index] != ')' and input_string[index] != '{' and input_string[index] != '}' and input_string[index] != ']' and input_string[index] != '[':
            new_string = new_string + (' ') 
        else:
            new_string = new_string + (input_string[index])
    string = new_string.replace(' ', '')
    length = len(string)
    final_len = len(string) - 1
    while final_len != length:
        length = len(string)
        string = string.replace('[]', '')
        string = string.replace('{}', '')
        string = string.replace('()', '')
        final_len = len(string)
    if string == "":
        result = True
    return result