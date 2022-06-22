PRIME=[2,3,5,7]

def prime(number):
    for index in range(10,105000):
        is_prime = True
        for element in PRIME:
            if index % element == 0:
                is_prime = False
        if is_prime == True:
            # print(index)
            PRIME.append(index)
    return '", "'.join(PRIME)

print(prime(10001))