
def is_isogram(string):
    string = string.replace('-', '')
    string = string.replace(' ', '')
    string = string.casefold()
    letters_used = [0] * len(string)
    for index in range(len(string)):
        for char in string.casefold():
            if string[index] == char:
                letters_used[index] = letters_used[index] + 1
    result = True
    print(letters_used)
    for number in letters_used:
        if number != 1 : result = False

    return result
        