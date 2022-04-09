def square_of_sum(number):
    i = 1
    sum = 0
    while i <= number:
        sum = sum + i
        i = i + 1
    square_sum = sum ** 2
    return square_sum


def sum_of_squares(number):
    i = 1
    sum = 0
    while i <= number:
        sum = sum + (i**2)
        i = i + 1
    return sum


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
