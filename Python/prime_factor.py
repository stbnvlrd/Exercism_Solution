def factors(value):
    factors_list =[]
    count = 0
    max_factor = 900000
    print(value)
    x = 2
    while value != 1:
        while value % x == 0: 
            value = value / x
            count = count + 1
            factors_list.append(x)
            print(value)
        x = x + 1
    return factors_list
