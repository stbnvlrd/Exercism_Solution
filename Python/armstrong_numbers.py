def is_armstrong_number(number):
    number_str = str(number)
    exp = len(number_str)
    number_sum = 0
    for x in number_str:
        number_sum =  number_sum + (int(x) ** exp)
    return number == number_sum