def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    factors = []
    poss_products = []

    value = 0
    for index in range(max_factor, min_factor-1, -1):
        factors.append(index)
    print(len(factors))
    for factor1 in factors:
        for factor2 in factors:
            poss_products.append(factor1 * factor2)
    print(len(poss_products))
    for index in poss_products:
        test_num = str(index)
        if len(test_num) == 8 or len(test_num) == 9:
            if test_num[-1] == test_num[0] and test_num[-2] == test_num[1] and test_num[-3] == test_num[2] and test_num[-4] == test_num[3] and value < int(test_num):
                value = int(test_num)
        if len(test_num) == 6 or len(test_num) == 7:
            if test_num[-1] == test_num[0] and test_num[-2] == test_num[1] and test_num[-3] == test_num[2] and value < int(test_num):
                value = int(test_num)
        if len(test_num) == 4 or len(test_num) == 5:
            if test_num[-1] == test_num[0] and test_num[-2] == test_num[1] and value < int(test_num):
                value = int(test_num)
        if len(test_num) < 4:
            if test_num[-1] == test_num[0] and value < int(test_num):
                value = int(test_num)
    print(value)

    return value

def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    factors = []
    poss_products = []

    value = 9999999
    for index in range(max_factor, min_factor-1, -1):
        factors.append(index)
    print(len(factors))
    for factor1 in factors:
        for factor2 in factors:
            poss_products.append(factor1 * factor2)
    print(len(poss_products))
    for index in poss_products:
        test_num = str(index)
        if len(test_num) == 8 or len(test_num) == 9:
            if test_num[-1] == test_num[0] and test_num[-2] == test_num[1] and test_num[-3] == test_num[2] and test_num[-4] == test_num[3] and value > int(test_num):
                value = int(test_num)
        if len(test_num) == 6 or len(test_num) == 7:
            if test_num[-1] == test_num[0] and test_num[-2] == test_num[1] and test_num[-3] == test_num[2] and value > int(test_num):
                value = int(test_num)
        if len(test_num) == 4 or len(test_num) == 5:
            if test_num[-1] == test_num[0] and test_num[-2] == test_num[1] and value > int(test_num):
                value = int(test_num)
        if len(test_num) < 4:
            if test_num[-1] == test_num[0] and value > int(test_num):
                value = int(test_num)
    print(value)

    return value

# largest(1000, 9999)
smallest(1000, 9999)