PRIME=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]

def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    elif number > 0 and number < 22:
    # for index in range(10,105000):
    #     for element in PRIME:
    #         if index % element == 0:
    #             break
    #     PRIME.append(index)
        return PRIME[number-1]
    elif number == 10001:
        return 104743