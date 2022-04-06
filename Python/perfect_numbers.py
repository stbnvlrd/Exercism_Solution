def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number > 0:
        sum = 0
        for x in range(1, number):
            if number % x == 0:
                sum = sum + x
    else:
        raise ValueError("Classification is only possible for positive integers.")
    if sum == number:
        result = "perfect"
    elif sum > number:
        result = "abundant"
    else:
        result = "deficient"
    return result
