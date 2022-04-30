def is_valid(isbn):
    sum = 0
    new_isbn = isbn.replace('-', '')

    for index in range(len(new_isbn)):
        if index == 9 and new_isbn[index] == "X":
            number = 10
        elif new_isbn[index].isnumeric():
            number = new_isbn[index]
        elif not new_isbn[index].isnumeric():
            sum = 0.1
            break
        sum = sum + (int(number) * (10 - index))
    if sum % 11 == 0 and len(new_isbn) == 10:
        result = True
    else:
        result = False
    return result